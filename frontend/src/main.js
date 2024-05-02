import {
    createVuesticEssential, VaButton, VaIcon, VaCard, VaCardTitle, VaCardContent, VaLayout,
    VaSidebar, 
    VaNavbar,
    VaNavbarItem,
    VaSidebarItemTitle,
    VaSidebarItem,
    VaSidebarItemContent, 
    VaCarousel,
    VaConfig,
    VaModal,
    VaForm,
    VaInput,
    VaCounter,
    VaOptionList,
    VaCheckbox,
    VaSelect,
    VaFileUpload,
    VaDateInput,
    VaAvatar,
    VaImage} from 'vuestic-ui';

import 'vuestic-ui/styles/essential.css';
import 'vuestic-ui/styles/typography.css'
import './assets/main.css';


import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)


app.use(createVuesticEssential({ 
    components: { 
        VaButton, VaIcon, VaCard, VaCardTitle, VaCardContent,
        VaLayout, VaSidebar, VaNavbar, VaNavbarItem, VaSidebarItemTitle, 
        VaSidebarItem, VaSidebarItemContent, VaCarousel, VaConfig, VaModal, VaForm,
    VaInput, VaDateInput, VaCounter,VaOptionList, VaCheckbox, VaSelect, VaFileUpload, VaAvatar,
    VaImage
},
}));
app.mount('#app')
