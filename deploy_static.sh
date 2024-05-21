#!/usr/bin/env bash

# Define the hosts for Fabric
hosts=('54.172.4.252' '54.175.109.84')

# Retrieve the RSA file as cmd arg
key_file="$1"

# Define the base directory as the script's directory
base_dir=$(dirname "$0")

log() {
    echo "$(date +"%Y-%m-%d %H:%M:%S") - $1"
}

do_pack() {
    log "Packing the npm build..."
    # Get the current date and time in the format YYYYMMDDHHMMSS
    current_date=$(date +"%Y%m%d%H%M%S")
    # If the versions/ directory does not exist, create it
    versions_dir="${base_dir}/versions"
    if [ ! -d "${versions_dir}" ]; then
        mkdir "${versions_dir}"
    fi
    # Define the name of the archive file
    file_name="${versions_dir}/npm_build_${current_date}.tgz"
    # Create a .tgz archive of the npm build
    tar -cvzf "${file_name}" -C "${base_dir}/frontend/dist" .
    if [ $? -ne 0 ]; then
        log "Failed to pack the npm build."
        return 1
    fi
    if [ -f "${file_name}" ]; then
        log "Packed npm build into ${file_name}"
        # Return the name of the archive file
        echo "${file_name}"
    else
        log "Archive file ${file_name} was not created."
        return 1
    fi
}

do_deploy() {
    archive_path="$1"
    host="$2"
    log "Deploying ${archive_path} to ${host}..."
    # Check if the archive file exists
    if [ ! -f "${archive_path}" ]; then
        log "Archive file ${archive_path} does not exist."
        return 1
    fi
    # Get the name of the archive file
    file_n=$(basename "${archive_path}")
    # Get the name of the archive file without the extension
    no_ext="${file_n%.*}"

    # Define the path to the releases directory
    path="/var/www/unity-tree/releases/"
    # Upload the archive to the /tmp directory on the web server
    scp -i "${key_file}" "${archive_path}" "${host}:/tmp/"
    if [ $? -ne 0 ]; then
        log "Failed to upload archive to ${host}."
        return 1
    fi

    # Create a new directory for the archive in the releases directory
    ssh -i "${key_file}" "${host}" "mkdir -p ${path}${no_ext}/"
    if [ $? -ne 0 ]; then
        log "Failed to create directory on ${host}."
        return 1
    fi

    # Extract the archive to the new directory
    ssh -i "${key_file}" "${host}" "tar -xzf /tmp/${file_n} -C ${path}${no_ext}/"
    if [ $? -ne 0 ]; then
        log "Failed to extract archive on ${host}."
        return 1
    fi

    # Remove the archive from the /tmp directory
    ssh -i "${key_file}" "${host}" "rm /tmp/${file_n}"
    if [ $? -ne 0 ]; then
        log "Failed to remove archive from /tmp on ${host}."
        return 1
    fi

    # Remove the current symbolic link
    ssh -i "${key_file}" "${host}" "rm -rf /var/www/unity-tree/current"
    if [ $? -ne 0 ]; then
        log "Failed to remove current symbolic link on ${host}."
        return 1
    fi

    # Create a new symbolic link to the new directory
    ssh -i "${key_file}" "${host}" "ln -s ${path}${no_ext}/ /var/www/unity-tree/current"
    if [ $? -ne 0 ]; then
        log "Failed to create new symbolic link on ${host}."
        return 1
    fi

    log "Successfully deployed ${archive_path} to ${host}."
    return 0
}

deploy() {
    # Call do_pack to create the archive
    archive_path=$(do_pack)
    if [ $? -ne 0 ]; then
        log "Failed to pack the project."
        return 1
    fi

    # If do_pack returned None (i.e., the archive was not created), return False
    if [ -z "${archive_path}" ]; then
        log "No archive was created."
        return 1
    fi

    # Call do_deploy to distribute the archive and return its result
    for host in "${hosts[@]}"; do
        do_deploy "${archive_path}" "${host}"
        if [ $? -ne 0 ]; then
            log "Deployment to ${host} failed."
            return 1
        fi
    done
    log "Deployment to all hosts succeeded."
    return 0
}

deploy
result=$?

if [ $result -ne 0 ]; then
    log "Deployment script failed."
else
    log "Deployment script succeeded."
fi

