<script setup>
    import { ref } from 'vue';
    import marqueeComponent from './marqueeComponent.vue';
    

    // user avatar configuration
    const avatarSizeConfig  ={
        "sizes": {
            "large": 150
        }
    }

    // static user info
    const userInfo = ref({
        "name": "C-3PO",
        "dateOfBirth": new Date(1877, 2, 14).toDateString(),
        "img": "https://randomuser.me/api/portraits/men/1.jpg",
        "role":"parent"
    })

    // calculates the users birthday
    function calculateAge(dateOfBirth) {
    let today = new Date();
    let birthDate = new Date(dateOfBirth);
    let age = today.getFullYear() - birthDate.getFullYear();
    let monthDifference = today.getMonth() - birthDate.getMonth();

    // Adjust the age if the current month is before the birth month or it's the birth month but the day hasn't occurred yet
    if (monthDifference < 0 || (monthDifference === 0 && today.getDate() < birthDate.getDate())) {
        age--;
    }

    return age;
    }


</script>
<template>
    
    <div class="header-section">

        <VaAvatar size="large" :sizes-config="avatarSizeConfig"
        :src='userInfo.img'/>
   
        <div class="right-header">
            <h2>{{ userInfo.name }}</h2>
            <p>Born: {{ userInfo.dateOfBirth }}</p>
            <p>Age: {{ calculateAge(userInfo.dateOfBirth) }}</p>
            
        </div>
    </div>

    <div class="gallery-section">
        <h3>Memories</h3>
        <marqueeComponent />
    </div>

</template>

<style scoped lang="scss">

//header section styles
.header-section{
    display: grid;
    grid-template-columns: 1fr 2fr;
    column-gap: 20px ;
    justify-items:center;
    align-items: center;
    margin: auto;
    width: 50%;
    height: auto;
    padding-bottom: 50px;
    border-bottom: solid 1px black;
    
    .right-header{
        width: 100%;
        p{
            padding: 0;
            margin: 0;
        }
        
    }

    .glow {
        -webkit-animation: glow 1s ease-in-out infinite alternate;
        -moz-animation: glow 1s ease-in-out infinite alternate;
        animation: glow 1s ease-in-out infinite alternate;
    }
    @keyframes glow {
        from {
            box-shadow: 0 0 10px #00ff00, 0 0 20px #00ff00, 0 0 30px #00ff00, 0 0 40px #00ff00;
        }
        to {
            box-shadow: 0 0 20px #00ff00, 0 0 30px #ff00de, 0 0 40px #ff00de, 0 0 50px #ff00de, 0 0 60px #ff00de;
        }
    }
}

.gallery-section{
    margin: auto;
    width: 75%;
    padding-bottom: 20px;
    border-bottom: solid 1px black;
}



.siblings-section {
    background-color: aqua;
}
.description-section{
    background-color: red;
}

.autobiography-section{
    background-color: chartreuse;
}

@media (max-width: 600px){

    .header-section {
        grid-template-columns: 1fr;
        align-items: center;
        row-gap:10px;
    }
}


</style>