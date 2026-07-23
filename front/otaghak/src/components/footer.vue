<template>
  <div class="footer mt-5">
    <div class="footer-container d-flex justify-content-center p-3">
      <div class="contain d-flex">
        <div class="row w-100">

          <!-- بخش چپ -->
          <div class="left d-flex flex-column align-items-center col-5">

            <div
              class="community mt-5 text-white align-items-center rounded-3 w-75 p-3 d-flex justify-content-center gap-2"
            >
              <span class="fs-5 fw-bold">@ava_shn</span>
              <span>ارتباط با پشتیبانی در ایتا</span>
              <span><i class="bi bi-telephone-outbound"></i></span>
            </div>

            <div class="Validity d-flex gap-3 mt-4">
              <img src="./../../New_folder/nemad.png" alt="" class="img">
              <img src="./../../New_folder/etehad.png" alt="" class="img">
              <img src="./../../New_folder/gerd.png" alt="" class="img">
              <img src="./../../New_folder/saz.png" alt="" class="img">
              <img src="./../../New_folder/saman.png" alt="" class="img">
            </div>
          </div>

          <!-- بخش راست -->
          <div class="right col-7 d-flex flex-column">

            <div class="header gap-3 w-100 d-flex flex-column align-items-end p-3">
              <span class="d-flex gap-2 align-items-center">
                <span>سامانه پناه</span>
                <img src="../../New_folder/logo.jpg" alt="" class="logo">
              </span>
            </div>

            <div class="link d-flex flex-column align-items-end w-100">
              <span>لینک‌های پرکاربرد</span>

              <div class="links mt-4 d-flex justify-content-between w-50">

                <div class="left d-flex flex-column align-items-end gap-3">

                  <router-link to="/reservation-rules" class="detail">
                    قوانین و مقررات رزرو
                  </router-link>

                  <router-link to="/host" class="detail">
                    قوانین و راهنمای میزبان
                  </router-link>

                  <router-link to="/quality-policy" class="detail">
                    خط مشی کیفیت پناه
                  </router-link>

                </div>

                <div class="right d-flex flex-column align-items-end gap-3">

                  <router-link to="/support" class="detail">
                    تماس با ما
                  </router-link>

                  <router-link to="/host" class="detail">
                    میزبان شوید
                  </router-link>

                  <router-link to="/about" class="detail">
                    درباره پناه
                  </router-link>

                </div>

              </div>
            </div>

          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>

<style>
@import '../assets/header.css';
</style>