<template>
  <div class="speed d-flex justify-content-center">
        <div class="speed-container ">
            <div class="swiper-container d-flex flex-column align-items-center  ">
            <div class="up w-100 d-flex  align-items-end ">
                <div class="button w-50">
                    <div class="lower-swiper-wrapper position-relative ms-5 mb-3">
                    <button class="custom-prevy rounded-2 position-absolute"><i class="bi bi-caret-left"></i></button>
                    <button class="custom-nexty rounded-2 position-absolute"><i class="bi bi-caret-right"></i></button>
                    </div>
                </div>
                <div class="text  text-white w-50 d-flex flex-column align-items-end p-2  gap-3">
                    <span class="fs-5 fw-bold">جستجوی سریع</span>
                    <span class="fw-normal">تجربه اقامتی جذاب با تنوع اقامتگاه ها</span>
                </div>
               
            </div>
            <div class="down ">
                <swiper
                :modules="[Navigation]"
                :slides-per-view="6"
                :space-between="12"
                :navigation="{ nextEl: '.custom-nexty', prevEl: '.custom-prevy' }"
                class="custom-swiper p-4">
                <swiper-slide class="img d-flex flex-column rounded-2"><img src="./../../New_folder/ram.jpeg" alt="Image 1" class="img-fluid rounded-3"/>
                <span class="text-end  p-2">رامسر</span>
            </swiper-slide>
                <swiper-slide class="img d-flex flex-column rounded-2">
                    <img src="./../../New_folder/masa.jpeg" alt="Image 2" class="img-fluid rounded-3"/>
                <span class="text-end p-2">ماسال</span>
            </swiper-slide>
                <swiper-slide class="img d-flex flex-column rounded-2 "><img src="./../../New_folder/kord.jpeg" alt="Image 3" class="img-fluid rounded-3"/>
                <span class="text-end p-2">کردان</span>
            </swiper-slide>
                <swiper-slide class="img d-flex flex-column rounded-2 "><img src="./../../New_folder/tehr.jpeg" alt="Image 1" class="img-fluid rounded-3"/>
                <span class="text-end p-2">تهران</span>
            </swiper-slide>
                <swiper-slide class="img d-flex flex-column rounded-2 "><img src="./../../New_folder/banda.jpeg" alt="Image 2" class="img-fluid rounded-3"/>
                <span class="text-end p-2">بندر انزلی</span>
            </swiper-slide>
                <swiper-slide class="img d-flex flex-column rounded-3 "><img src="./../../New_folder/mahmo.jpeg" alt="Image 3" class="img-fluid rounded-3"/>
                <span class="text-end p-2">محمود آباد</span>
            </swiper-slide>
                <swiper-slide class="img d-flex flex-column rounded-3 "><img src="./../../New_folder/chal.jpeg" alt="Image 1" class="img-fluid rounded-3"/>
                <span class="text-end p-2">چالوس</span>
            </swiper-slide>
                <swiper-slide class="img d-flex flex-column "><img src="./../../New_folder/kish.jpeg" alt="Image 2" class="img-fluid rounded-3"/>
                <span class="text-end p-2">کیش</span>
            </swiper-slide>
                <swiper-slide class="img d-flex flex-column rounded-3 "><img src="./../../New_folder/rash.jpeg" alt="Image 3" class="img-fluid rounded-3"/>
                <span class="text-end p-2">رشت</span>
            </swiper-slide>

                <swiper-slide class="img d-flex flex-column  rounded-3 "><img src="./../../New_folder/nosh.jpeg" alt="Image 3" class="img-fluid rounded-3"/>
                    <span class="op text-end p-2">نوشهر</span>
                </swiper-slide>
            </swiper>
   
            </div>
                
                
           
        </div>
        </div>
    </div>
</template>

<script setup>
import { Swiper, SwiperSlide } from 'swiper/vue';
import { Navigation, Autoplay } from "swiper/modules";
import 'swiper/css';
import 'swiper/css/navigation';

</script>


<style>
@import '../assets/header.css';
</style>