import { createRouter,createWebHistory } from "vue-router";
import main from '../components/main.vue'
import Rooms from '../components/room.vue'
import profile from "@/components/profile.vue";
import Login from '../components/Login.vue';
import HostRegister from '../components/HostRegister.vue';
import Support from '../components/Support.vue';

const routes=[ 
    {path:'/', component:main},
    {path:'/room', component:Rooms},
    {path:'/profile',component:profile}, 
    {path:'/login', component:Login},
    {path:'/host', component:HostRegister},
    {path:'/support', component:Support},

]
const router = createRouter({history: createWebHistory(), routes})


export default router