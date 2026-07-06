<template>
    <div class="destination d-flex justify-content-center  ">
        <div class="destination-container ">
            <div class="swiper-container  ">
                <div class="ms-5 d-flex gap-2">
                <button class="custom-prev rounded-2 d-flex justify-content-center align-items-center"><i class="bi bi-caret-left"></i></button>
                <button class="custom-next rounded-2 d-flex justify-content-center align-items-center"><i class="bi bi-caret-right"></i></button>
                
                </div>
            <swiper
                :modules="[Navigation]"
                :slides-per-view="6"
                :space-between="2"
                :navigation="{ nextEl: '.custom-next', prevEl: '.custom-prev' }"
                class="custom-swiper   p-4 ">
                <swiper-slide class="img d-flex flex-column align-items-end"@click="selectCity('رامسر')"><img src="./../../New_folder/ram.jpeg" alt="Image 1" class="img-fluid rounded-3"/>
                <span>رامسر</span>
            </swiper-slide>
                <swiper-slide class="img d-flex flex-column align-items-end"@click="selectCity('ماسال')">
                    <img src="./../../New_folder/masa.jpeg" alt="Image 2" class="img-fluid rounded-3"/>
                <span>ماسال</span>
            </swiper-slide>
                <swiper-slide class="img d-flex flex-column align-items-end"@click="selectCity('کردان')"><img src="./../../New_folder/kord.jpeg" alt="Image 3" class="img-fluid rounded-3"/>
                <span>کردان</span>
            </swiper-slide>
                <swiper-slide class="img d-flex flex-column align-items-end"@click="selectCity('تهران')"><img src="./../../New_folder/tehr.jpeg" alt="Image 1" class="img-fluid rounded-3"/>
                <span>تهران</span>
            </swiper-slide>
                <swiper-slide class="img d-flex flex-column align-items-end"@click="selectCity('بندر انزلی')" ><img src="./../../New_folder/banda.jpeg" alt="Image 2" class="img-fluid rounded-3"/>
                <span>بندر انزلی</span>
            </swiper-slide>
                <swiper-slide class="img d-flex flex-column align-items-end" @click="selectCity('محمود آباد')"><img src="./../../New_folder/mahmo.jpeg" alt="Image 3" class="img-fluid rounded-3"/>
                <span>محمود آباد</span>
            </swiper-slide>
                <swiper-slide class="img d-flex flex-column align-items-end"@click="selectCity('چالوس')"><img src="./../../New_folder/chal.jpeg" alt="Image 1" class="img-fluid rounded-3"/>
                <span>چالوس</span>
            </swiper-slide>
                <swiper-slide class="img d-flex flex-column align-items-end"@click="selectCity('کیش')"><img src="./../../New_folder/kish.jpeg" alt="Image 2" class="img-fluid rounded-3"/>
                <span>کیش</span>
            </swiper-slide>
                <swiper-slide class="img d-flex flex-column align-items-end"@click="selectCity('رشت')"><img src="./../../New_folder/rash.jpeg" alt="Image 3" class="img-fluid rounded-3"/>
                <span>رشت</span>
            </swiper-slide>

                <swiper-slide class="img d-flex flex-column align-items-end"@click="selectCity('نوشهر')"><img src="./../../New_folder/nosh.jpeg" alt="Image 3" class="img-fluid rounded-3"/>
                    <span class="op">نوشهر</span>

                </swiper-slide>
            </swiper>
   
             </div>
        </div>  
    </div>

</template>

<script setup>
import { Swiper, SwiperSlide } from 'swiper/vue';
import { Navigation, Autoplay } from "swiper/modules";
import 'swiper/css';
import 'swiper/css/navigation';
import { defineEmits } from "vue";
import itemRoom from './itemRoom.vue'
import { ref } from "vue";
const emit = defineEmits(["select-city"]);

const selectCity = (city) => {
  emit("select-city", city);
};
</script>

<style>
@import '../assets/header.css';
</style>