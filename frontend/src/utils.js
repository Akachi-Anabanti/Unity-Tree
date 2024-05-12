export const getLocalToken = () => {
    return localStorage.getItem('token')
};


export const getCookie = (name) =>{
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

export const saveLocalToken = (token) => {
    localStorage.setItem('token', token)
};

export const removeLocalToken = () => {
    localStorage.removeItem('token')
};
