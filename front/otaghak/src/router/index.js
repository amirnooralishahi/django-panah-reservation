import { createRouter,createWebHashHistory } from "vue-router";
import main from '../components/main.vue'
import profile from "@/components/profile.vue";
import Login from '../components/Login.vue';
import HostRegister from '../components/HostRegister.vue';
import Support from '../components/Support.vue';
import Register from '../components/Register.vue';
import RoomDetail from '../components/RoomDetail.vue';

const routes=[ 
    {path:'/', component:main},
    {path:'/room', component:main},
    {path:'/room/:id', component:RoomDetail, props:true, name:'room-detail'},
    {path:'/profile',component:profile}, 
    {path:'/login', component:Login},
    {path:'/register', component:Register},
    {path:'/host', component:HostRegister},
    {path:'/support', component:Support},

]
const router = createRouter({history: createWebHashHistory(), routes})


export default router