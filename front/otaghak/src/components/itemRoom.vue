<template>

     <div class="swiper-wrapper">      
<swiper-slide v-for="(image, index) in props.imagearr" :key="index">
        <img :src="image" alt="تصویر" class="img-fluid rounded-3" />
</swiper-slide>
</div>
  
 
</template>

<script setup>

import { Swiper, SwiperSlide } from 'swiper/vue';
import { Navigation } from 'swiper/modules';
import 'swiper/css';
import 'swiper/css/navigation';
const props = defineProps({
    imagearr:Array,
  
});


console.log(props.imagearr);

</script>

<style>
@import '../assets/header.css';

</style>