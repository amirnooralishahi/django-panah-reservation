<template>
    <Header />
    <div class="header d-flex justify-content-center">
      <div class="header-container d-flex  p-3">
        <div  class="left w-50 d-flex gap-4 ">
            <div class="left d-flex gap-2 align-items-center">
                <span>افزودن به علاقه مندی </span><span><i class="bi bi-heart"></i></span>
            </div>
            <div class="right d-flex gap-2 align-items-center">
                <span>اشتراک گذاری </span><span><i class="bi bi-share"></i></span>
            </div>
          

        </div>
        <div class="right w-50 d-flex justify-content-between align-items-center">
          <div class="d-flex gap-4 "    id='pic'>
            <div id="border"
              v-for="(item, index) in items"
              :key="index"
              class="text d-flex flex-column-reverse align-items-center p-2   gap-2"
              :class="{ active : activeIndex === index}"
              
              @click="handleClick(index)"
            >
            <div 
              class="d-flex border"
              :class="{ line : activeIndex === index  }"
            
              ></div>
           
              {{ item }}
             
            </div>
          </div>
          <div class="d-flex gap-1 align-items-center">
            <span class="fs-5 fw-bold">
              2473266
            </span>
            <span>: شناسه</span>
          </div>
        </div>
      </div>
    </div>
    
    <div class="images w-100 border d-flex justify-content-center">
        <div class="images-container  d-flex">
            <div class="left w-50 h-100  d-flex flex-column border gap-2">
                <div class=" w-100 h-50 d-flex gap-2">
                    <img src="../../New_folder/room/326a8c93-9f7a-4230-9384-2f04672d0dfe.webp" alt="" class=" w-50 h-100 img1 img2">
                <img src="../../New_folder/room/3d2e8edd-ea3f-43d1-a150-c527f0dd2a00.webp" alt="" class=" w-50 h-100 img2">
                
                </div>
                <div class="w-100 h-50 d-flex gap-2">
                    <div class="w-50 h-100 position-relative  image">
                    <img src="../../New_folder/room/51264bea-af1d-435f-9ec4-9c09f6c0627a.webp" alt="" class=" position-absolute w-100 h-100 img img2">
                        <div class="rel text-white d-flex align-items-center justify-content-center  position-absolute">
                            <span><i class="bi bi-caret-left"></i></span>   
                            <span class="text"> مشاهده همه تصاویر </span>
                    
                        </div>
                    </div>
                <img src="../../New_folder/room/653fe732-7139-4ac5-a519-0d9ad1c301b7.webp" alt="" class=" w-50 h-100 img2">
                </div>
                
            </div>
            <div class="right w-50  border h-100">

                <img src="../../New_folder/room/1.webp" alt="" class="img-fluid h-100 rounded-end">

            </div>

        </div>
    </div>
    <div  class="body d-flex justify-content-center mt-4">
        <div class="body-container d-flex row rounded-3">
            <div @click="not" class="right col-8 p-1" dir="rtl">
                <div class="titleHome">
                    <div>
                        <h5>
                        استخردار آبگرم رهام با ایرهاکی، در ماهدشت 
                    </h5>
                    </div>
                    <div class="d-flex gap-2 align-items-center">
                        <span><i class="bi bi-key-fill"></i></span>
                        <span>دربست</span>
                        <span><i class="bi bi-exclamation-circle"></i></span>

                    </div>
                <div class="d-flex justify-content-between">
                    <div class="detail d-flex gap-2">
                        <div class="right">
                            <img src="../../New_folder/room/joz.png" alt="" class="img rounded-circle">
                        </div>
                        <div class="left d-flex flex-column gap-2 justify-content-center">
                            <span class="textDetail fw-bold">
                                محمد علی جوزانی
                            </span>
                            <span class="textDetail text">کمتر از 1 سال میزبان اتاقک </span>
                        </div>
                    </div>
                    <div class="point">
                        <div class="star d-flex gap-1 align-items-center">
                            <span ><i class="bi bi-star-fill gold"></i></span>
                            <span class="fs-5">5.0</span>
                             <span class="text ">(1نظر)</span>
                        </div>
                        <div class="succes d-flex align-items-center gap-1">
                            <span><i class="bi bi-check-circle circle"></i></span>
                            <span class="fs-5">24</span>
                            <span class="text">رزرو موفق</span>
                        </div>
                        
                        <div class="succes d-flex align-items-center gap-1">
                            <span><i class="bi bi-emoji-smile"></i></span>
                            <span class="fs-5">% 100 </span>
                            <span class="text"> توصیه شده </span>
                        </div>
                    </div>
                    
                </div>
                <div class="line w-100"></div>

                </div>
                <div class="about mt-5">
                    <div class="about-container d-flex flex-column gap-3">
                        <span class="fw-bold">درباره اقامتگاه</span>
                        <div class="d-flex align-items-center gap-3">
                            <span class="fs-4"><i class="bi bi-house"></i></span>
                            <div class="d-flex flex-column gap-2 ">
                                <span class="fw-bold ">اطلاعات بنا</span>
                                <div class="d-flex gap-2 info">
                                    <span>120 متر </span>
                                    <span>2اتاق</span>
                                    <span>فلت</span>
                                    <span>پارکینگ روباز</span>
                                </div>
                            </div>
                        </div>
                        <div class="d-flex align-items-center gap-3">
                            <span class="fs-4"><i class="bi bi-truck-flatbed"></i></span>
                            <div class="d-flex flex-column gap-2 ">
                                <span class="fw-bold">سرویس خواب</span>
                                <div class="info ">
                                    <span>2 تخت دو نفره</span>
                                    <span> 2 سرویس خواب کامل</span>
                                </div>
                            </div>
                        </div>
                        <div class="d-flex align-items-center gap-3">
                            <span class="fs-4"><i class="bi bi-bar-chart-steps"></i></span>
                            <div class="d-flex flex-column gap-2 ">
                                <span class="fw-bold">دسترسی پذیری </span>
                                <div class="info ">
                                    <span>همکف</span>
                                    <span> 3 تا 5 پله  </span>
                                    <span>بدون آسانسور</span>

                                </div>
                            </div>
                        </div>
                        <div class="d-flex align-items-center gap-3">
                            <span class="fs-4"><i class="bi bi-truck-flatbed"></i></span>
                            <div class="d-flex flex-column gap-2 ">
                                <span class="fw-bold">سرویس بهداشتی و حمام </span>
                                <div class="info ">
                                    <span>1 توالت فرنگی  </span>
                                    <span> 1 دوش در سرویس </span>
                                </div>
                            </div>
                        </div>
                        <div class="d-flex align-items-center gap-3">
                            <span class="fs-4"><i class="bi bi-person"></i></span>
                            <div class="d-flex flex-column gap-2 ">
                                <span class="fw-bold">ظرفیت اقامتگاه </span>
                                <div class="info ">
                                    <span>6 نفر پایه </span>
                                    <span> 14 نفر اضافه </span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="line w-100 mt-4"></div>
                <div class="pool">
                    <div class="pool-container d-flex flex-column gap-3">
                        <span>اقامتگاه های استخردار  </span>
                        <div class="d-flex gap-2 align-items-center">
                            <span>
                                <img alt="otaghak.com" loading="lazy" width="32" height="32" decoding="async" data-nimg="1" class="w-6 h-6 md:w-8 md:h-8" style="color: transparent;" src="https://cdn.otaghak.com/otg-images/Web/Icon/ic_OutdoorPool.svg">   
                            </span>
                            <span class="text">استخر روباز بیرون ساختمان</span>
                        </div>
                        <div class="detail d-flex gap-3 ">
                            <div class="squar rounded-3 border p-2 d-flex flex-column align-items-center justify-content-center">
                                <span>ابعاد</span>
                                <span class="text-black"> 6*4</span>
                            </div>
                            <div class="squar rounded-3 border p-2 d-flex flex-column align-items-center justify-content-center">
                                <span>دمای آب </span>
                                <span class="text-black text-down">آب گرم </span>
                            </div>
                            <div class="squar rounded-3 border p-2 d-flex flex-column align-items-center justify-content-center">
                                <span>عمق</span>
                                <span class="text-black text-down"> از 1.3 تا 1.7 متر</span>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="line w-100 mt-4"></div>
                <div class="sleep">
                    <div class="sleep-container d-flex flex-column gap-4">
                    <span>فضای خواب</span>
                    <div class="pack d-flex flex-column gap-2">
                        <div class="d-flex">
                            
                        <span class="title fw-bold">هال و پذیرایی یک </span>

                        </div>
                        <div class=" d-flex gap-2">
                            <div class="squar rounded-3 border p-2 d-flex flex-column gap-2 justify-content-center">
                                    <span class="sys">سیستم گرمایشی </span>
                                    <span class="text-black"> اسپیلت</span>
                            </div>
                            <div class="squar rounded-3 border p-2 d-flex flex-column  gap-2 justify-content-center">
                                <span class="sys">سیستم گرمایشی</span>
                                <span class="text-black">شوفاژ</span>
                            </div>
                        </div>
                     </div>
                     <div class="pack d-flex flex-column gap-2">
                        <div class="d-flex">
                            
                        <span class="title fw-bold">اتاق خواب یک </span>

                        </div>
                        <div class=" d-flex gap-2">
                            <div class="squar rounded-3 border p-2 d-flex flex-column gap-2 justify-content-center">
                                    <span class="sys">سرویس خواب</span>
                                    <span class="text-black"> تخت دو نفره </span>
                            </div>
                            <div class="squar rounded-3 border p-2 d-flex flex-column  gap-2 justify-content-center">
                                <span class="sys">سیستم گرمایشی</span>
                                <span class="text-black">شوفاژ</span>
                            </div>
                        </div>
                     </div>
                     <div class="pack d-flex flex-column gap-2">
                        <div class="d-flex">
                            
                        <span class="title fw-bold" >اتاق خواب دو - اتاق مستر </span>

                        </div>
                        <div class=" d-flex gap-2">
                            <div class="squar rounded-3 border p-2 d-flex flex-column gap-2 justify-content-center">
                                    <span class="sys">سرویس خواب </span>
                                    <span class="text-black"> تخت دو نفره</span>
                            </div>
                            <div class="squar rounded-3 border p-2 d-flex flex-column  gap-2 justify-content-center">
                                <span class="sys">سیستم گرمایشی</span>
                                <span class="text-black">شوفاژ</span>
                            </div>
                        </div>
                     </div>
                </div>
                 </div>
                 <div class="line w-100 mt-4"></div>
                 <div class="Facilities w-100">
                    <div class="Facilities-container d-flex flex-column w-50 p-2 ">
                        <span>امکانات اقامتگاه</span>
                        <div class="d-flex justify-content-between mt-3 ">
                                <div class="d-flex flex-column gap-3">
                                <div class="d-flex align-items-center gap-2">
                                    <span>
                                        <img alt="otaghak.com" loading="lazy" width="24" height="24" decoding="async" data-nimg="1" class="w-6 h-6 md:w-7 md:h-7" style="color: transparent;" src="https://cdn.otaghak.com/otg-images/Web/Icon/ic_gas.svg">   
                                    </span>
                                    <span>اجاق گاز </span>
                                </div>
                                <div class="d-flex align-items-center gap-2">
                                    <span><i class="bi bi-speaker"></i></span>
                                    <span>سیستم صوتی</span>
                                </div>
                                <div class="d-flex align-items-center gap-2">
                                    <span>
                                        <img alt="otaghak.com" loading="lazy" width="24" height="24" decoding="async" data-nimg="1" class="w-6 h-6 md:w-7 md:h-7" style="color: transparent;" src="https://cdn.otaghak.com/otg-images/Web/Icon/ic_microwave.svg">                            </span>
                                    <span> فر/مایکروویو</span>
                                </div>
                                <div class="d-flex align-items-center gap-2"> 
                                    <span>
                                        <img alt="otaghak.com" loading="lazy" width="24" height="24" decoding="async" data-nimg="1" class="w-6 h-6 md:w-7 md:h-7" style="color: transparent;" src="https://cdn.otaghak.com/otg-images/Web/Icon/ic_foosball.svg">
                                    </span>
                                    <span>
                                        فوتبال دستی 
                                    </span>
                                </div>
                                </div>
                                 <div class="d-flex flex-column gap-3">
                                <div class="d-flex align-items-center gap-2">
                                    <span>
                                        <img alt="otaghak.com" loading="lazy" width="24" height="24" decoding="async" data-nimg="1" class="w-6 h-6 md:w-7 md:h-7" style="color: transparent;" src="https://cdn.otaghak.com/otg-images/Web/Icon/ic_ref.svg">
                                    </span>
                                    <span>یخچال</span>
                                </div>
                                <div class="d-flex align-items-center gap-2">
                                    <span><i class="bi bi-tv"></i></span>
                                    <span>تلویزیون</span>
                                </div>
                                <div class="d-flex align-items-center gap-2">
                                    <span>
                                        <img alt="otaghak.com" loading="lazy" width="24" height="24" decoding="async" data-nimg="1" class="w-6 h-6 md:w-7 md:h-7" style="color: transparent;" src="https://cdn.otaghak.com/otg-images/Web/Icon/ic_canape.svg">
                                    </span>
                                    <span>مبلمان</span>
                                </div>
                                </div>
                        </div>
                        <div @click="allView" class="view d-flex gap-2 align-items-center  mt-3 ">
                            <span class="hover">مشاهده همه امکانات</span>
                            <i class="bi bi-caret-left hover"></i>
                            <span></span>
                        </div>
                     <!-- پنل امکانات اقامتگاه -->
                    <div v-if="vie" class="allView position-fixed   w-100 h-100" style="z-index: 1050; ">
                    <!-- پنل سمت راست -->
                    <div class="  d-flex flex-column position-absolute end-0 bg-white w-50 h-100">
                        
                        <!-- هدر ثابت بالا -->
                        <div class="p-3 bg-white shadow-sm position-sticky top-0 z-3">
                        <div class="d-flex justify-content-between align-items-center">
                            <span @click="closeView" class="border p-1 rounded" style="cursor: pointer;">
                            <i class="bi bi-x-lg"></i>
                            </span>
                            <span class="fw-bold">امکانات اقامتگاه</span>
                        </div>
                        </div>

                        <!-- محتوای اسکرول‌پذیر -->
                        <div class="flex-grow-1 overflow-auto px-3">

                        <!-- بخش سرویس بهداشتی -->
                        <div class="py-3 border-bottom">
                            <span class="fw-bold">سرویس بهداشتی و حمام</span>
                            <div class="mt-3 d-flex gap-2 align-items-center">
                            <img src="https://cdn.otaghak.com/otg-images/Web/Icon/Bath-Room-Area-Icon.svg" width="28" />
                            <span>سرویس بهداشتی</span>
                            </div>
                            <div class="ps-4">روشویی، توالت فرنگی، دوش</div>
                        </div>

                        <!-- لوازم خانگی -->
                        <div class="py-3 border-bottom">
                            <span class="fw-bold">لوازم خانگی</span>
                            <div class="mt-3 d-flex flex-column gap-2">
                            <div class="d-flex gap-2 align-items-center">
                                <img src="https://cdn.otaghak.com/otg-images/Web/Icon/ic_canape.svg" width="28" />
                                <span>مبلمان</span>
                            </div>
                            <div class="d-flex gap-2 align-items-center">
                                <img src="https://cdn.otaghak.com/otg-images/Web/Icon/ic_tv.svg" width="28" />
                                <span>تلویزیون</span>
                            </div>
                            <div class="d-flex gap-2 align-items-center">
                                <img src="https://cdn.otaghak.com/otg-images/Web/Icon/ic_MizNaharkhori.svg" width="28" />
                                <span>میز نهارخوری</span>
                            </div>
                            <div class="d-flex gap-2 align-items-center">
                                <img src="https://cdn.otaghak.com/otg-images/Web/Icon/ic_player.svg" width="28" />
                                <span>سیستم صوتی</span>
                            </div>
                            <div class="d-flex gap-2 align-items-center">
                                <img src="https://cdn.otaghak.com/otg-images/Web/Icon/ic_Jaroobarghi.svg" width="28" />
                                <span>جارو برقی</span>
                            </div>
                            </div>
                        </div>

                        <!-- امکانات آشپزی -->
                        <div class="py-3 border-bottom">
                            <span class="fw-bold">امکانات آشپزی</span>
                            <div class="mt-3 d-flex flex-column gap-2">
                            <div class="d-flex gap-2 align-items-center" v-for="item in cookingItems" :key="item.text">
                                <img :src="item.icon" width="28" />
                                <span>{{ item.text }}</span>
                            </div>
                            </div>
                        </div>

                        <!-- امکانات رفاهی -->
                        <div class="py-3 border-bottom">
                            <span class="fw-bold">امکانات رفاهی</span>
                            <div class="mt-3 d-flex gap-2 align-items-center">
                            <img src="https://cdn.otaghak.com/otg-images/Web/Icon/ic_kebab.svg" width="28" />
                            <span>سیخ و منقل کباب</span>
                            </div>
                        </div>

                        <!-- امکانات تفریحی -->
                        <div class="py-3 border-bottom">
                            <span class="fw-bold">امکانات تفریحی</span>
                            <div class="mt-3 d-flex flex-column gap-2">
                            <div class="d-flex gap-2 align-items-center">
                                <img src="https://cdn.otaghak.com/otg-images/Web/Icon/ic_foosball.svg" width="28" />
                                <span>فوتبال دستی</span>
                            </div>
                            <div class="d-flex gap-2 align-items-center">
                                <img src="https://cdn.otaghak.com/otg-images/Web/Icon/ic_AirHockey-3.svg" width="28" />
                                <span>ایرهاکی</span>
                            </div>
                            </div>
                        </div>

                        <!-- امکانات امنیتی -->
                        <div class="py-3 border-bottom">
                            <span class="fw-bold">امکانات امنیتی</span>
                            <div class="mt-3 d-flex flex-column gap-2">
                            <div v-for="item in securityItems" :key="item.text" class="d-flex gap-2 align-items-center">
                                <img :src="item.icon" width="28" />
                                <span>{{ item.text }}</span>
                            </div>
                            </div>
                        </div>

                        <!-- امکانات ساختمان -->
                        <div class="py-3 border-bottom">
                            <span class="fw-bold">امکانات ساختمان</span>
                            <div class="mt-3 d-flex flex-column gap-3">
                            <div class="d-flex gap-2 align-items-center">
                                <img src="https://cdn.otaghak.com/otg-images/Web/Icon/ic_Teras-Balkon-3.svg" width="28" />
                                <span>تراس دارد</span>
                            </div>
                            <div class="d-flex gap-2 align-items-center">
                                <img src="https://cdn.otaghak.com/otg-images/Web/Icon/ic_Garden.svg" width="28" />
                                <span>700 متر درخت‌کاری شده</span>
                            </div>
                            <div class="d-flex gap-2 align-items-center">
                                <img src="https://cdn.otaghak.com/otg-images/Web/Icon/ic_alter_icon.svg" width="28" />
                                <span>آلاچیق تاشو کنار استخر</span>
                            </div>
                            </div>
                        </div>

                        <!-- پارکینگ -->
                        <div class="py-3 border-bottom">
                            <span class="fw-bold">پارکینگ</span>
                            <div class="mt-3 d-flex gap-2 align-items-center">
                            <img src="https://cdn.otaghak.com/otg-images/Web/Icon/ic_ParkingRoobaz.svg" width="28" />
                            <span>پارکینگ روباز برای ۵ خودرو</span>
                            </div>
                        </div>

                        <!-- استخر -->
                        <div class="py-3 border-bottom">
                            <span class="fw-bold">استخر</span>
                            <div class="mt-3 d-flex flex-column gap-1">
                            <div class="d-flex gap-2 align-items-center">
                                <img src="https://cdn.otaghak.com/otg-images/Web/Icon/ic_OutdoorPool.svg" width="28" />
                                <span>استخر روباز با آب گرم</span>
                            </div>
                            <small class="ps-4">ابعاد: ۴×۶ متر، عمق ۱.۳ تا ۱.۷ متر</small>
                            </div>
                        </div>

                        </div>
                    </div>
                    </div>

                  
                 </div>
                </div>
                <div class="line w-100 mt-4"></div>
                <div class="status mt-5">
                    <div class="status-container">
                        <span>وضعیت آنتن دهی </span>
                        <div class="d-flex mt-3 gap-5">
                            <div class="d-flex gap-3 align-items-center">
                                <span><img alt="اتاقک" fetchpriority="high" width="28" height="28" decoding="async" data-nimg="1" class="iconSize" style="color: transparent;" src="https://cdn.otaghak.com/otg-images/Web/Icon/ic_HamrahAval.svg"></span>
                                <div class="d-flex flex-column">
                                    <span class="fw-bold">همراه اول</span>
                                    <span>عالی / 5G / 4.5G </span>
                                </div>
                            </div>
                            <div class="d-flex gap-3 align-items-center">
                                <span><img alt="اتاقک" fetchpriority="high" width="28" height="28" decoding="async" data-nimg="1" class="iconSize" style="color: transparent;" src="https://cdn.otaghak.com/otg-images/Web/Icon/ic_Irancell.svg"></span>
                                <div class="d-flex flex-column ">
                                    <span class="fw-bold">ایرانسل</span>
                                    <span>عالی /5G/4.5G </span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="line w-100 mt-4"></div>
                <div class="rent">
                    <div class="rent-container d-flex flex-column gap-4">
                        <span class="fw-bold">اجاره روزانه و ماهانه استخردار آبگرم رهام با ایرهاکی، 120 متر برای 6 نفر به همراه 14 نفر اضافی در شهر ماهدشت با تضمین بهترین کیفیت و قیمت در اتاقک</span>
                        <span class="text fw-lighter">ویلا رهام با استخر آبگرم اقامتگاهی برای آرامش و تفریح شماست. این ویلا در زمینی به مساحت 1000 متر مربع با زیر بنای 120 متر مربع در منطقه ماهدشت واقع شده است. ویلا فلت بوده و دارای دو اتاق خواب، حمام و سرویس بهداشتی فرنگی است. حیاط ویلا برای پارک 5 خودرو مناسب است. ویلا مناسب تردد سالمند، کودک و افراد دارای معلولیت است. پذیرش حیوان خانگی در این ویلا فقط در فضای باز مجاز است. </span>
                        <div @click="refah" class="d-flex gap-2 align-items-center">
                            <span class="hover">
                                نمایش جزئیات بیشتر 
                            </span>
                            <span class="hover"><i class="bi bi-caret-left-fill"></i></span>
                        </div>
                            <div v-if="refahi"  class="allView position-fixed   w-100 h-100" style="z-index: 1050; ">
                    <!-- پنل سمت راست -->
                    <div class="  d-flex flex-column position-absolute end-0 bg-white w-50 h-100">
                        
                        <!-- هدر ثابت بالا -->
                        <div class="p-3 bg-white shadow-sm 3">
                        <div class="d-flex justify-content-between align-items-center">
                            <span @click="closer" class="border p-1 rounded" style="cursor: pointer;">
                            <i class="bi bi-x-lg"></i>
                            </span>
                            <span class="fw-bold">امکانات اقامتگاه</span>
                        </div>
                        </div>

                        <!-- محتوای اسکرول‌پذیر -->
                        <div class="flex-grow-1 overflow-auto px-3">

                        <!-- بخش سرویس بهداشتی -->
                        <div class="py-3 border-bottom d-flex flex-column gap-3">
                            <span class="fw-bold">
                                اجاره روزانه و ماهانه استخردار آبگرم رهام با ایرهاکی، 120 متر برای 6 نفر به همراه 14 نفر اضافی در شهر ماهدشت با تضمین بهترین کیفیت و قیمت در اتاقک
                            </span>
                            <span class="moj ">
                                ویلا رهام با استخر آبگرم اقامتگاهی برای آرامش و تفریح شماست. این ویلا در زمینی به مساحت 1000 متر مربع با زیر بنای 120 متر مربع در منطقه ماهدشت واقع شده است. ویلا فلت بوده و دارای دو اتاق خواب، حمام و سرویس بهداشتی فرنگی است. حیاط ویلا برای پارک 5 خودرو مناسب است. ویلا مناسب تردد سالمند، کودک و افراد دارای معلولیت است. پذیرش حیوان خانگی در این ویلا فقط در فضای باز مجاز است. 
                            </span>
                        </div>
                        <div class="py-3 border-bottom d-flex flex-column gap-3">
                            <span class="fw-bold">
                                امکانات اقامتگاه : 
                            </span>
                            <div class="d-flex flex-column gap-3">
                                <span>
                                    - استخر آبگرم 
                                </span>
                                <span>
                                     - سالن بازی دارای فوتبال دستی 
                                </span>
                                <span>
                                    - آشپزخانه با امکانات رفاهی شامل اجاق گاز، یخچال ، فریزر و لوازم آشپزی -
                                </span>
                                <span>
                                   - اتاق پذیرایی دارای مبلمان، تلویزیون و سیستم صوتی -
                                </span>
                                <span>
                                  -  سیستم سرمایشی کولر گازی و گرمایشی شوفاژ -
                                </span>
                            </div>
                        </div>
                        
                       

                        </div>
                    </div>
                             </div>
                            


                    </div>
                </div>
                <div class="location">
                                <div class="location-container d-flex flex-column gap-3">
                                    <span class="fw-bold">
                                        موقعیت تقریبی اقامتگاه
                                    </span>
                              <!-- بخش موقعیت اقامتگاه -->
                                    <div class="map-section">
                                    <!-- پیام اطلاع‌رسانی -->
                                    <span class="note">
                                        آدرس و موقعیت دقیق اقامتگاه، پس از رزرو برای شما ارسال خواهد شد
                                    </span>

                                    <!-- کانتینر نقشه و عنوان -->
                                    <div class="map-container-wrapper">
                                        <!-- عنوان بخش -->
                                        <h2 class="section-title">
                                        موقعیت تقریبی اقامتگاه
                                        </h2>

                                        <!-- توضیح زیر عنوان -->
                                        <div class="map-description mb-3">
                                        <span class="caption">
                                            آدرس و موقعیت دقیق اقامتگاه، پس از رزرو برای شما ارسال خواهد شد
                                        </span>
                                        </div>

                                        <!-- نقشه -->
                                        <div id="map" class="map-container"></div>
                                    </div>
                                    </div>

                                </div>
                </div>
                <div class="line w-100 mt-4"></div>

                <div class="center w-100 p-4">
                <div class="center-container d-flex flex-column gap-4 w-50">
                    <span class="fw-bold fs-5">مراکز نزدیک</span>
                    <div class=" d-flex  justify-content-between align-items-center">
                        <div class="d-flex flex-column gap-2">
                            <span >سوپر مارکت</span>
                            <span class="text">پیاده : کمتر از 10 دقیقه</span>
                            <span class="text">  با ماشین : کمتر از 5 دقیق</span>
                        </div>
                        <div class="d-flex flex-column gap-2">
                            <span>نانوایی </span>
                            <span class="text">پیاده : کمتر از 10 دقیقه</span>
                            <span class="text">
                                با ماشین : کمتر از 5 دقیقه
                            </span>
                        </div>
                    </div>
                </div>
                </div>
                <div class="line w-100 mt-4"></div>
                    <div class="calculate p-4">
                        <div class="calculate-container d-flex flex-column gap-3">
                        <span class="fw-bold">محاسبه قیمت</span>
                        <div  class="d-flex gap-2">
                            <span><img alt="اتاقک" fetchpriority="high" width="28" height="28" decoding="async" data-nimg="1" class="iconSize" style="color: transparent;" src="https://cdn.otaghak.com/otg-images/Web/Icon/kid.svg"></span>
                            <div class="d-flex flex-column">
                                <span class="fw-bold">نرخ ورود کودک </span>
                                <span class="text">تا 1 کودک زیر 3 سال در صورتحساب لحاظ نمی گردد </span>
                            </div>
                        </div>
                        <div  class="d-flex gap-2">
                            <span><img alt="اتاقک" fetchpriority="high" width="28" height="28" decoding="async" data-nimg="1" class="iconSize" style="color: transparent;" src="https://cdn.otaghak.com/otg-images/Web/Icon/extra-person.svg"></span>
                            <div class="d-flex flex-column">
                                <span class="fw-bold">نرخ هر نفر اضافه </span>
                                <span class="text">350/000 تومان </span>
                            </div>
                        </div>       
                        </div>
                    </div>
                <div class="line w-100 mt-4"></div>
                    <div class="taghvim">
                        <div class="taghvim-container d-flex flex-column gap-4 p-3">
                            <span class="fw-bold">تقویم و نرخ رزرو </span>
                            <div  id="his" class="history-calender bg-white  rounded-3 " style="">
                            <div class="history-calender-container d-flex flex-column p-2 gap-2">

                          
                                <div class="month">
                                    <div class="month-container d-flex w-100 ">
                                       
                                       
                                        <div v-if="!next" class="farvardin d-flex flex-column w-50 gap-2 align-items-end">
                                            <div class="d-flex gap-2 w-100 align-items-center">
                                                <span v-if="next">
                                                    <i class="bi bi-caret-left mark"></i>
                                                </span>
                                                <div class="d-flex  ms-5 gap-2 w-75 justify-content-center align-items-center fw-bold">
                                                
                                                    <span class="fs-5">1404</span>
                                                <span>فروردین</span>

                                                </div>
                                                <div class="d-flex w-25">
                                                <span>
                                                    <i class="bi bi-caret-right mark"></i>
                                                </span>
                                                </div>
                                                
                                            </div>
                                            <div class="days d-flex gap-2 justify-content-center w-100">
                                                <span> جمعه</span>
                                                <span>پنج شنبه</span>
                                                <span>چهارشنبه</span>
                                                <span> سه شنبه</span>
                                                <span>دوشنبه</span>
                                                <span>یک شنبه</span>
                                                <span>شنبه</span>
                                            </div>

                                            <div  class=" day d-flex flex-row-reverse justify-content-end   w-100   row">
                                                    <div class=" d-flex flex-column align-items-start w-100 ">
                                                        <div class="d-flex flex-column align-items-center ">
                                                            <span>1</span>
                                                        <span>2/500 </span>
                                                        </div>
                                                        
                                                    </div>
                                                <div  class=" items gap-2 row d-flex flex-row-reverse   w-100 ">
                                                
                                                <div v-for="(item, index) in number" :key="index"
                                                class="item   d-flex flex-column  align-items-center "
                                                 :class="{am : ((item)%7)==1, ab: (item<=16)}" >
                                                 <div v-if="item<=31">
                                                 {{ item }}
                                                 <div class="" v-if="item>15">
                                                   
                                                   2/500
                                         
                                               </div>
                                                 </div>
                                                 

                                                </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="ordi d-flex flex-column w-50 gap-2 align-items-end">
                                            <div class="d-flex gap-2 w-100 align-items-center">
                                                <div class="d-flex w-25">
                                              
                                                <div v-if="next">
                                                    <i class="bi bi-caret-right mark bg-white" @click="perFunct"></i>
                                                </div>
                                                </div>
                                                <div class="d-flex  gap-2 w-75 justify-content-start align-items-center fw-bold">
                                                <span class="fs-5">1404</span>
                                                <span>اردیبهشت</span>

                                                </div>
                                                <div v-if="!next" @click="nextfunc">
                                                    <i class="bi bi-caret-left mark bg-white"></i>
                                                </div>
                                               
                                            </div>
                                            <div class="days d-flex gap-2 justify-content-center w-100">
                                                <span> جمعه</span>
                                                <span>پنج شنبه</span>
                                                <span>چهارشنبه</span>
                                                <span> سه شنبه</span>
                                                <span>دوشنبه</span>
                                                <span>یک شنبه</span>
                                                <span>شنبه</span>
                                            </div>

                                            <div  class=" day d-flex flex-row-reverse justify-content-end   w-100   row">
                                                    <div class=" d-flex flex-column align-items-start w-100 ">
                                                        <div class="d-flex flex-column align-items-center ">
                                                            <span>1</span>
                                                        <span>2/500 </span>
                                                        </div>
                                                        
                                                    </div>
                                                <div  class=" items gap-2 row d-flex flex-row-reverse   w-100 ">
                                                
                                                <div v-for="(item, index) in number" :key="index"
                                                class="item    d-flex flex-column  align-items-center "
                                                 :class="{am : ((item)%7)==1, ab: (item<=16)}" >
                                                 <div v-if="item<=31">
                                                 {{ item }}
                                                 <div class="" v-if="item>15">
                                                   
                                                   2/500
                                         
                                               </div>
                                                 </div>
                                                 

                                                </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div v-if="next" class="khordad d-flex flex-column w-50 gap-2 align-items-end">
                                            <div class="d-flex gap-2 w-100 align-items-center">
                                                <div v-if="!next" class="d-flex w-25">
                                                    <i class="bi bi-caret-right mark"></i>
                                                </div>
                                                <div class="d-flex  gap-2 w-75 justify-content-center align-items-center fw-bold">
                                                <span class="fs-5">1404</span>
                                                <span>خرداد</span>

                                                </div>
                                             
                                                <div v-if="next"  class="border">
                                                    <i class="bi bi-caret-left mark bg-white"></i>
                                                </div>
                                            </div>
                                            <div class="days d-flex gap-2 justify-content-center w-100">
                                                <span> جمعه</span>
                                                <span>پنج شنبه</span>
                                                <span>چهارشنبه</span>
                                                <span> سه شنبه</span>
                                                <span>دوشنبه</span>
                                                <span>یک شنبه</span>
                                                <span>شنبه</span>
                                            </div>

                                            <div  class=" day d-flex flex-row-reverse justify-content-end   w-100   row">
                                                    <div class=" d-flex flex-column align-items-start w-100 ">
                                                        <div class="d-flex flex-column align-items-center ">
                                                            <span>1</span>
                                                        <span>2/500 </span>
                                                        </div>
                                                        
                                                    </div>
                                                <div  class=" items gap-2 row d-flex flex-row-reverse   w-100 ">
                                                
                                                <div v-for="(item, index) in number" :key="index"
                                                class="item    d-flex flex-column  align-items-center "
                                                 :class="{am : ((item)%7)==1, ab: (item<=16)}" >
                                                 <div v-if="item<=31">
                                                 {{ item }}
                                                 <div class="" v-if="item>15">
                                                   
                                                   2/500
                                         
                                               </div>
                                                 </div>
                                                 

                                                </div>
                                                </div>
                                            </div>
                                        </div>
                                     
                                    </div>
                                </div>
                         
                            
                            </div>
                           
                       
                       </div>
                        <div class="reserve mt-2">
                            <div class="d-flex flex-column gap-2">
                                <div class="d-flex gap-2 align-items-center">
                                <span><img alt="اتاقک" loading="lazy" width="20" height="20" decoding="async" data-nimg="1" style="color: transparent;" src="https://cdn.otaghak.com/otg-images-new/Web/Icon/general/instant-booking-gold.svg"></span>
                                <span class="text">رزرو سریع اقامتگاه بدون نیاز به تایید میزبان </span>
                            </div>
                            <div class="d-flex gap-2 align-items-center">
                                <span><img alt="اتاقک" loading="lazy" width="24" height="24" decoding="async" data-nimg="1" style="color: transparent;" src="https://cdn.otaghak.com/otg-images-new/Web/Icon/general/alert-icon.svg"></span>
                                <span class="text"> قیمت ها به هزار تومان است. (3 صفر حذف شده) </span>
                            </div>
                            </div>
                            
                        </div>   
                        <div class="accept">
                                    <div class="d-flex accept-container w-100">
                                        <div class="left w-50">
                                            <button class="but rounded-3 text-white d-flex justify-content-center align-items-center">
پاک کردن انتخاب                                             </button>
                                       
                                        </div>
                                        <div class="right w-50 d-flex justify-content-end  align-items-center">
                                            <div class="guid d-flex gap-2 align-items-center ">
                                                <span><i class="bi bi-question-circle"></i></span>

                                                <span>راهنمای تقویم</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                    </div>
                    </div>
                <div class="line w-100 mt-4"></div>
                    <div class="time">
                        <div class="time-container">
                            <span class="fw-bold">مقررات زماانی اقامتگاه </span>
                        <div class="d-flex gap-3">
                            <div class="pack d-flex flex-column gap-2">
                        <div class="d-flex">
                            
                        <span class="title fw-bold">هال و پذیرایی یک </span>

                        </div>
                        <div class=" d-flex gap-2">
                            <div class="squar rounded-3 border p-2 d-flex flex-column gap-2 justify-content-center">
                                <div class="d-flex gap-2 align-items-center">
                                    <span><img alt="اتاقک" fetchpriority="high" width="24" height="24" decoding="async" data-nimg="1" class="w-5 h-5 md:w-6 md:h-6" style="color: transparent;" src="https://cdn.otaghak.com/otg-images/Web/Icon/calendar.svg"></span>

                                <span class="sys">زمان ورود  </span>
                                </div>    
                                    <span class="text-black">ساعت 14:00 تا 22:00</span>
                            </div>
                            <div class="squar rounded-3  p-2  d-flex  flex-column align-items-start  gap-2">
                                <div class="close d-flex gap-2 align-items-center  border ">
                                <span><img alt="اتاقک" fetchpriority="high" width="24" height="24" decoding="async" data-nimg="1" class="w-5 h-5 md:w-6 md:h-6" style="color: transparent;" src="https://cdn.otaghak.com/otg-images/Web/Icon/calendar.svg"></span>
                                <span class="sys">زمان خروج</span>

                                </div>
                                
                                <span class="text-black">ساعت 12:00</span>
                            </div>
                        </div>
                         </div>
                       
                        </div>
                            <div class="fix d-flex flex-column gap-3 mt-4">
                                <span class="fw-bold">قوانین اقامتگاه </span>
                                <div class="d-flex flex-column gap-2">
                                    <div class="d-flex gap-2 align-items-center">
                                        <span><img alt="otaghak" loading="lazy" width="28" height="28" decoding="async" data-nimg="1" class="w-6 h-6 md:w-7 md:h-7" style="color: transparent;" src="https://cdn.otaghak.com/otg-images/Web/Icon/PetNotAllowed.svg"></span>
                                        <span class="text">ورود حیوان خانگی مجاز نیست</span>
                                    </div>
                                    <div class="d-flex gap-2 align-items-center">
                                        <span><img alt="otaghak" loading="lazy" width="28" height="28" decoding="async" data-nimg="1" class="w-6 h-6 md:w-7 md:h-7" style="color: transparent;" src="https://cdn.otaghak.com/otg-images/Web/Icon/PartyNotAllowed.svg"></span>
                                        <span class="text">برگزاری مراسم مجاز نیست</span>
                                    </div>
                                    <div class="d-flex gap-2 align-items-center">
                                        <span> <img alt="otaghak" loading="lazy" width="28" height="28" decoding="async" data-nimg="1" class="w-6 h-6 md:w-7 md:h-7" style="color: transparent;" src="https://cdn.otaghak.com/otg-images/Web/Icon/NoneMarriedGroupsAllowed.svg"></span>
                                        <span class="text">جمع های مجردی کاملا مجاز و آزاد است </span>
                                    </div>
                                    <div class="d-flex gap-2 align-items-center">
                                        <span><img alt="otaghak" loading="lazy" width="28" height="28" decoding="async" data-nimg="1" class="w-6 h-6 md:w-7 md:h-7" style="color: transparent;" src="https://cdn.otaghak.com/otg-images/Web/Icon/SmokingAllowed.svg"></span>
                                        <span class="text">استعمال دخانیات کاملا مجاز و آزاد است</span>
                                    </div>
                                    <div class="d-flex gap-2 align-items-center">
                                        <span><img alt="otaghak" loading="lazy" width="28" height="28" decoding="async" data-nimg="1" class="w-6 h-6 md:w-7 md:h-7" style="color: transparent;" src="https://cdn.otaghak.com/otg-images/Web/Icon/ShoesInsideBuildingNotAllowed.svg"></span>
                                        <span class="text">تردد با کفش داخل محیط ساختما مجاز نیست</span>
                                    </div>
                                    <div class="d-flex gap-2 align-items-center">
                                        <span><img alt="otaghak" loading="lazy" width="28" height="28" decoding="async" data-nimg="1" class="w-6 h-6 md:w-7 md:h-7" style="color: transparent;" src="https://cdn.otaghak.com/otg-images/Web/Icon/YardUsageNotAllowed.svg"></span>
                                        <span class="text">استفاده از حیاط و باغ مجاز نیست</span>
                                    </div>
                                    <div class="d-flex gap-2 align-items-center"> 
                                        <span><img alt="otaghak" loading="lazy" width="28" height="28" decoding="async" data-nimg="1" class="w-6 h-6 md:w-7 md:h-7" style="color: transparent;" src="https://cdn.otaghak.com/otg-images/Web/Icon/IdentityDocumentNationalCard.svg"></span>
                                        <span class="text">کارت شناسایی معتبر کافی است </span>
                                    </div>
                                </div>
                            </div>
                            <div class="miz mt-4 d-flex flex-column gap-3">
                                <span class="fw-bold">قوانین میزبان</span>
                                <div class="d-flex align-items-end gap-2">
                                    <span><img alt="otaghak" loading="lazy" width="24" height="24" decoding="async" data-nimg="1" class="w-6 h-6 md:w-7 md:h-7" style="color: transparent;" src="https://cdn.otaghak.com/otg-images/Web/Icon/ic-hostrule.svg"></span>
                                    <span class="text">شستن ظرف ها الزامی است بردن زباله پس از اتمام رزرو الزامی است. </span>
                                </div>
                            </div>
                            <div class="cansel mt-4">
                                <div class="d-flex flex-column gap-4 ">
                                    <span class="fw-bold"> مقررات لغو رزرو</span>
                                    <span class="fw-bold">متعادل</span>
                                </div>
                                <div  class="dash d-flex align-items-center mt-4">
                                    <i class="bi bi-dash" v-for="(item,index) in  Array(55).fill().map((_, i) => i + 1)" :key="index"></i>
                                </div>
                                <div class="green d-flex flex-column gap-2 mt-4">
                                    <div class="d-flex gap-2 text-green align-items-center">
                                        <span><img alt="لغو رزرو تا 48 ساعت مانده به زمان ورود روز کنسل شده" loading="lazy" width="28" height="28" decoding="async" data-nimg="1" class="w-6 h-6 md:w-7 md:h-7" style="color: transparent;" src="https://cdn.otaghak.com/otg-images/Web/Icon/cancel-48.svg"></span>
                                        <span class="text"> لغو رزرو تا 48 ساعت مانده به زمان ورود روز کنسل شده </span>
                                    </div>
                                    <span class="price"> 15 درصد کل مبلغ رزرو</span>
                                </div>
                                <div  class="dash d-flex align-items-center mt-4">
                                    <i class="bi bi-dash" v-for="(item,index) in  Array(55).fill().map((_, i) => i + 1)" :key="index"></i>
                                </div>
                                <div class="yellow d-flex flex-column gap-2 mt-4">
                                    <div class="d-flex gap-2  align-items-center">
                                        <span><img alt="لغو رزرو در کمتر از 48 ساعت مانده به زمان ورود روز کنسل شده" loading="lazy" width="28" height="28" decoding="async" data-nimg="1" class="w-6 h-6 md:w-7 md:h-7" style="color: transparent;" src="https://cdn.otaghak.com/otg-images/Web/Icon/cancel-lt-48.svg"></span>
                                        <span class="text">  لغو رزرو در کمتر از 48 ساعت مانده به زمان ورود روز کنسل شده </span>
                                    </div>
                                    <span class="price">  100 درصد روزهایی که کمتر از 48 ساعت به آنها مانده است + 15 درصد باقی روز ها</span>
                                </div>
                                <div  class="dash d-flex align-items-center mt-4">
                                    <i class="bi bi-dash" v-for="(item,index) in  Array(55).fill().map((_, i) => i + 1)" :key="index"></i>
                                </div>
                                <div class="red d-flex flex-column gap-2 mt-4">
                                    <div class="d-flex gap-2  align-items-center">
                                        <span><img alt="لغو رزرو حین اقامت" loading="lazy" width="28" height="28" decoding="async" data-nimg="1" class="w-6 h-6 md:w-7 md:h-7" style="color: transparent;" src="https://cdn.otaghak.com/otg-images/Web/Icon/cancel-during.svg"></span>
                                        <span class="text"> لغو رزرو حین اقامت  </span>
                                    </div>
                                    <span class="price">100درصد  مبلغ رزرو همان روز و دو روز بعد +15 درصد مبلغ رزرو روزهای باقی مانده </span>
                                </div>
                            </div>

                        </div>

                    </div>
                <div class="line w-100 mt-4"></div>

                    <div class="bail d-flex flex-column gap-3 mt-4">
                        <span class="fw-bold">ضمانت و گارانتی اتاقک </span>
                        <span class="text">اتاقک به شما اطمینان می‌دهد تا اقامتگاهی که رزرو کرده‌اید را با مشخصات ثبت شده آن در زمان مقرر تحویل بگیرید و وجه واریزی شما نزد اتاقک محفوظ می‌ماند تا درپایان تجربه خوب اقامت با میزبان تسویه شود.</span>
                        <div class="d-flex border rounded-3 p-4 justify-content-between align-items-center">
                            <div class="d-flex gap-3 align-items-center">
                            <span><img alt="اتاقک" loading="lazy" width="28" height="28" decoding="async" data-nimg="1" style="color: transparent;" src="https://cdn.otaghak.com/otg-images-new/Web/Icon/general/warranty.svg"></span>
                            <span>ضمانت تحویل و نظافت</span>
                            </div>
                            <div @click="didFunc" class="did d-flex gap-2 align-items-center border">
                                <span>مشاهده</span>
                                <span>
                                    <i class="bi bi-caret-left"></i>

                                </span>
                            </div>
                        </div>
                        <div  v-if="did" class="allView position-fixed  rounded-3    w-50 h-100" style="z-index: 1050; ">
                    <!-- پنل سمت راست -->
                    <div class="  d-flex flex-column  position-absolute end-0 bg-white w-100 h-100">
                        
                        <!-- هدر ثابت بالا -->
                        <div class="p-3 bg-white shadow-sm 3">
                        <div class="d-flex  gap-2 align-items-center">
                            <span @click="closeDid" class="border p-1 rounded" style="cursor: pointer;">
                            <i class="bi bi-x-lg"></i>
                            </span>
                            <span class="fw-bold ">ضمانت تحویل و نظافت</span>
                        </div>
                        </div>
                        <div class="line"></div>
                        <!-- محتوای اسکرول‌پذیر -->
                        <div class="flex-grow-1 overflow-auto px-3">

                        <!-- بخش سرویس بهداشتی -->
                        <div class="py-3 border-bottom d-flex flex-column gap-3">
                            <div>
                                <span><img alt="اتاقک" loading="lazy" width="28" height="28" decoding="async" data-nimg="1" style="color: transparent;" src="https://cdn.otaghak.com/otg-images-new/Web/Icon/general/warranty.svg"></span>
                                <span class="fw-bold text-danger">
                                ضمانت تحویل و نظافت
                            </span>
                            </div>
                            
                            <span class=" ">
                                اتاقک به شما اطمینان می‌دهد تا اقامتگاهی که رزرو کرده‌اید را با مشخصات ثبت شده آن در زمان مقرر تحویل بگیرید و وجه واریزی شما نزد اتاقک محفوظ می‌ماند تا درپایان تجربه خوب اقامت با میزبان تسویه شود. 
                            </span>
                        </div>
                        <div class="py-3 border-bottom d-flex flex-column gap-3">
                          <div class="d-flex gap-2 align-items-center">
                            
                            <span><img alt="RoomGuarantee" loading="lazy" width="24" height="24" decoding="async" data-nimg="1" style="color: transparent;" src="https://cdn.otaghak.com/otg-images/Web/Icon/no-delivery.svg"></span>
                            <span class="fw-bold text-danger">
                               اقامتگاه به مهمان تحویل داده نشده است  
                            </span> 
                        </div>
                            
                           <span class="moj">اتاقک امانتدار مبلغ رزرو شما است. درصورتی‌که اقامتگاهِ رزرو شده، در تاریخ و ساعت درج شده در سند رزرو، به شما تحویل داده نشود، حداکثر تا ساعت 9 صبح روز بعد از تاریخ شروع رزرو، مهلت دارید با پیگیری از پشتیبانی سایت اتاقک فرایند بازگشت مبلغ رزرو را انجام دهید. (نکته: پس از پایان مهلت مذکور، امکان استرداد مبلغ پرداخت شده وجود ندارد. ).</span>
                        </div>
                        <div class="py-3 border-bottom d-flex flex-column gap-3">
                          <div class="d-flex gap-2 align-items-center">
                            
                            <span><img alt="RoomGuarantee" loading="lazy" width="24" height="24" decoding="async" data-nimg="1" style="color: transparent;" src="https://cdn.otaghak.com/otg-images/Web/Icon/no-matching-specs.svg"></span>
                            <span class="fw-bold text-danger">
                               اقامتگاه با مشخصات مطابقت ندارد  
                            </span> 
                        </div>
                            
                           <span class="moj">
                            درصورتی‌که اقامتگاه تحویل داده شده با مشخصات و آدرس ثبت شده در سند رزرو اختلاف فاحش داشته باشد، حداکثر تا 3 ساعت پس از ورود، مهلت دارید با پیگیری از پشتیبانی سایت اتاقک فرایند بازگشت مبلغ رزرو را انجام دهید. (پس از پایان مهلت مذکور، امکان استرداد مبلغ پرداخت شده وجود ندارد.) (اختلاف فاحش: اختلاف در امکانات اصلی اقامتگاه مانند استخر و نوع آن، تعداد اتاق خواب و غیره است.)
                           </span>
                        </div>
                        <div class="py-3 border-bottom d-flex flex-column gap-3">
                          <div class="d-flex gap-2 align-items-center">
                            
                            <span><img alt="RoomGuarantee" loading="lazy" width="24" height="24" decoding="async" data-nimg="1" style="color: transparent;" src="https://cdn.otaghak.com/otg-images/Web/Icon/dirty-uncln.svg"></span>
                            <span class="fw-bold text-danger">
                               اقامتگاه کثبف است و نظافت نشده است   
                            </span> 
                        </div>
                            
                           <span class="moj">
                            RoomGuarantee
اقامتگاه کثیف است و نظافت نشده است
درصورتی‌که اقامتگاه تحویل داده شده به شکل مناسب نظافت نشده و موارد عدم نظافت به راحتی مشهود است، حداکثر تا 3 ساعت پس از ورود، مهلت دارید با پیگیری از پشتیبانی سایت اتاقک فرایند بازگشت مبلغ رزرو را انجام دهید. (پس از پایان مهلت مذکور، امکان استرداد مبلغ پرداخت شده وجود ندارد.).
                           </span>
                        </div>
                        
                        </div>
                        <div class="w-100  d-flex justify-content-center p-3 ">
                            <button class="border rounded-3 p-3 bg-white  d-flex gap-2 align-items-end">
                                <span class="">
                                    <i class="bi bi-telephone-outbound"></i>    
                                </span>
                                <span>تماس با پشتیبانی</span>    
                            </button>
                        </div>
                    </div>
                        </div>
                    </div>
                    <div class="line w-100 mt-4"></div>
                    <div class="comment">
                        <div class="comment-container d-flex flex-column gap-3 p-3">
                            <span class="fw-bold mt-4">نظرات مهمان ها </span>
                            <div class="point d-flex flex-column gap-3">
                                <div class="header d-flex gap-2">
                                    <span class="star"><i class="bi bi-star-fill"></i></span>
                                    <span class="fw-bold">4.8 امتیاز </span>
                                    <span>(16 نظر)</span>
                                </div>
                                <div class="d-flex w-100 gap-3">
                                    <div class="d-flex w-50 flex-column gap-4">
                                    <div class="d-flex justify-content-between">
                                        <span>امنیت محله </span>
                                        <span>4.9/5</span>
                                    </div>
                                    <div class="d-flex justify-content-between">
                                        <span>نظافت و تمیزی </span>
                                        <span>4.8/5</span>
                                    </div>
                                    <div class="d-flex justify-content-between">
                                        <span>ارزش کلی اقامتگاه </span>
                                        <span>4.6/5</span>
                                    </div>
                                </div>
                                <div class="d-flex w-50 flex-column gap-4">
                                    <div class="d-flex justify-content-between">
                                        <span>پذیرش میزبان</span>
                                        <span>4.9/5</span>
                                    </div>
                                    <div class="d-flex justify-content-between">
                                        <span>ارتباط با میزبان</span>
                                        <span>4.9/5</span>
                                    </div>
                                    <div class="d-flex justify-content-between">
                                        <span>صحت اطلاعات</span>
                                        <span>4.9/5</span>
                                    </div>
                                </div>
                                </div>
                             
                            </div>
                            <div class="contain d-flex flex-column gap-3">
                                <div class="d-flex gap-3  justify-content-between">
                                    <div class="box border rounded-4 p-3 d-flex flex-column gap-2">
                                        <div class="name d-flex justify-content-between">
                                            <div class="d-flex gap-2 align-items-center">
                                                <div class="person fs-5 d-flex align-items-center justify-content-center">
                                                    <i class="bi bi-person"></i>  
                                                </div>
                                                <div class="d-flex flex-column gap-2">
                                                    <span class="first fw-bold">سعید</span>
                                                    <span class="his">اسفند 1403</span>
                                                </div>
                                            </div>
                                            <div class="d-flex gap-2 align-items-center">
                                                <span><i class="bi bi-star-fill"></i></span>
                                                <span class="fs-5">3.33</span>
                                            </div>
                                        </div>
                                        <span class="nor mt-3">درکل متوسط بود </span>
                                        <div class="line"></div>
                                        <div class="answerMiz d-flex flex-column gap-3">
                                            <span class="mizban">
                                                پاسخ میزبان
                                            </span>
                                            <span class="text">
                                                با احترام شما میتونستید به مواردی همچون: تمیزی و امنیت واحد تحویل به موقع خوش برخوردی میزبان احساس آرامش و بی آزاری همسایگان رو قیدکنید! برای ما تمیزی داخل خونه هنگام تحویل مهمه ن راه پله ها
                                            </span>
                                        </div>
                                    </div>
                                    <div class="box border rounded-4 p-3 d-flex flex-column gap-2">
                                        <div class="name d-flex justify-content-between">
                                            <div class="d-flex gap-2 align-items-center">
                                                <div class="person fs-5 d-flex align-items-center justify-content-center">
                                                    <i class="bi bi-person"></i>  
                                                </div>
                                                <div class="d-flex flex-column gap-2">
                                                    <span class="first fw-bold">سعید</span>
                                                    <span class="his">اسفند 1403</span>
                                                </div>
                                            </div>
                                            <div class="d-flex gap-2 align-items-center">
                                                <span><i class="bi bi-star-fill"></i></span>
                                                <span class="fs-5">3.33</span>
                                            </div>
                                        </div>
                                        <span class="nor mt-3">درکل متوسط بود </span>
                                        <div class="line"></div>
                                        <div class="answerMiz d-flex flex-column gap-3">
                                            <span class="mizban">
                                                پاسخ میزبان
                                            </span>
                                            <span class="text">
                                                با احترام شما میتونستید به مواردی همچون: تمیزی و امنیت واحد تحویل به موقع خوش برخوردی میزبان احساس آرامش و بی آزاری همسایگان رو قیدکنید! برای ما تمیزی داخل خونه هنگام تحویل مهمه ن راه پله ها
                                            </span>
                                        </div>
                                    </div>
                                </div>
                                <div class="d-flex gap-3  justify-content-between">
                                    <div class="box border rounded-4 p-3 d-flex flex-column gap-2">
                                        <div class="name d-flex justify-content-between">
                                            <div class="d-flex gap-2 align-items-center">
                                                <div class="person fs-5 d-flex align-items-center justify-content-center">
                                                    <i class="bi bi-person"></i>  
                                                </div>
                                                <div class="d-flex flex-column gap-2">
                                                    <span class="first fw-bold">سعید</span>
                                                    <span class="his">اسفند 1403</span>
                                                </div>
                                            </div>
                                            <div class="d-flex gap-2 align-items-center">
                                                <span><i class="bi bi-star-fill"></i></span>
                                                <span class="fs-5">3.33</span>
                                            </div>
                                        </div>
                                        <span class="nor mt-3">درکل متوسط بود </span>
                                        <div class="line"></div>
                                        <div class="answerMiz d-flex flex-column gap-3">
                                            <span class="mizban">
                                                پاسخ میزبان
                                            </span>
                                            <span class="text">
                                                با احترام شما میتونستید به مواردی همچون: تمیزی و امنیت واحد تحویل به موقع خوش برخوردی میزبان احساس آرامش و بی آزاری همسایگان رو قیدکنید! برای ما تمیزی داخل خونه هنگام تحویل مهمه ن راه پله ها
                                            </span>
                                        </div>
                                    </div>
                                    <div class="box border rounded-4 p-3 d-flex flex-column gap-2">
                                        <div class="name d-flex justify-content-between">
                                            <div class="d-flex gap-2 align-items-center">
                                                <div class="person fs-5 d-flex align-items-center justify-content-center">
                                                    <i class="bi bi-person"></i>  
                                                </div>
                                                <div class="d-flex flex-column gap-2">
                                                    <span class="first fw-bold">سعید</span>
                                                    <span class="his">اسفند 1403</span>
                                                </div>
                                            </div>
                                            <div class="d-flex gap-2 align-items-center">
                                                <span><i class="bi bi-star-fill"></i></span>
                                                <span class="fs-5">3.33</span>
                                            </div>
                                        </div>
                                        <span class="nor mt-3">درکل متوسط بود </span>
                                        <div class="line"></div>
                                        <div class="answerMiz d-flex flex-column gap-3">
                                            <span class="mizban">
                                                پاسخ میزبان
                                            </span>
                                            <span class="text">
                                                با احترام شما میتونستید به مواردی همچون: تمیزی و امنیت واحد تحویل به موقع خوش برخوردی میزبان احساس آرامش و بی آزاری همسایگان رو قیدکنید! برای ما تمیزی داخل خونه هنگام تحویل مهمه ن راه پله ها
                                            </span>
                                        </div>
                                    </div>
                                </div>
                                <div class="d-flex gap-3  justify-content-between">
                                    <div class="box border rounded-4 p-3 d-flex flex-column gap-2">
                                        <div class="name d-flex justify-content-between">
                                            <div class="d-flex gap-2 align-items-center">
                                                <div class="person fs-5 d-flex align-items-center justify-content-center">
                                                    <i class="bi bi-person"></i>  
                                                </div>
                                                <div class="d-flex flex-column gap-2">
                                                    <span class="first fw-bold">سعید</span>
                                                    <span class="his">اسفند 1403</span>
                                                </div>
                                            </div>
                                            <div class="d-flex gap-2 align-items-center">
                                                <span><i class="bi bi-star-fill"></i></span>
                                                <span class="fs-5">3.33</span>
                                            </div>
                                        </div>
                                        <span class="nor mt-3">درکل متوسط بود </span>
                                        <div class="line"></div>
                                        <div class="answerMiz d-flex flex-column gap-3">
                                            <span class="mizban">
                                                پاسخ میزبان
                                            </span>
                                            <span class="text">
                                                با احترام شما میتونستید به مواردی همچون: تمیزی و امنیت واحد تحویل به موقع خوش برخوردی میزبان احساس آرامش و بی آزاری همسایگان رو قیدکنید! برای ما تمیزی داخل خونه هنگام تحویل مهمه ن راه پله ها
                                            </span>
                                        </div>
                                    </div>
                                    <div class="box border rounded-4 p-3 d-flex flex-column gap-2">
                                        <div class="name d-flex justify-content-between">
                                            <div class="d-flex gap-2 align-items-center">
                                                <div class="person fs-5 d-flex align-items-center justify-content-center">
                                                    <i class="bi bi-person"></i>  
                                                </div>
                                                <div class="d-flex flex-column gap-2">
                                                    <span class="first fw-bold">سعید</span>
                                                    <span class="his">اسفند 1403</span>
                                                </div>
                                            </div>
                                            <div class="d-flex gap-2 align-items-center">
                                                <span><i class="bi bi-star-fill"></i></span>
                                                <span class="fs-5">3.33</span>
                                            </div>
                                        </div>
                                        <span class="nor mt-3">درکل متوسط بود </span>
                                        <div class="line"></div>
                                        <div class="answerMiz d-flex flex-column gap-3">
                                            <span class="mizban">
                                                پاسخ میزبان
                                            </span>
                                            <span class="text">
                                                با احترام شما میتونستید به مواردی همچون: تمیزی و امنیت واحد تحویل به موقع خوش برخوردی میزبان احساس آرامش و بی آزاری همسایگان رو قیدکنید! برای ما تمیزی داخل خونه هنگام تحویل مهمه ن راه پله ها
                                            </span>
                                        </div>
                                    </div>
                                </div>
                                <div class="d-flex gap-3  justify-content-between">
                                    <div class="box border rounded-4 p-3 d-flex flex-column gap-2">
                                        <div class="name d-flex justify-content-between">
                                            <div class="d-flex gap-2 align-items-center">
                                                <div class="person fs-5 d-flex align-items-center justify-content-center">
                                                    <i class="bi bi-person"></i>  
                                                </div>
                                                <div class="d-flex flex-column gap-2">
                                                    <span class="first fw-bold">سعید</span>
                                                    <span class="his">اسفند 1403</span>
                                                </div>
                                            </div>
                                            <div class="d-flex gap-2 align-items-center">
                                                <span><i class="bi bi-star-fill"></i></span>
                                                <span class="fs-5">3.33</span>
                                            </div>
                                        </div>
                                        <span class="nor mt-3">درکل متوسط بود </span>
                                        <div class="line"></div>
                                        <div class="answerMiz d-flex flex-column gap-3">
                                            <span class="mizban">
                                                پاسخ میزبان
                                            </span>
                                            <span class="text">
                                                با احترام شما میتونستید به مواردی همچون: تمیزی و امنیت واحد تحویل به موقع خوش برخوردی میزبان احساس آرامش و بی آزاری همسایگان رو قیدکنید! برای ما تمیزی داخل خونه هنگام تحویل مهمه ن راه پله ها
                                            </span>
                                        </div>
                                    </div>
                                    <div class="box border rounded-4 p-3 d-flex flex-column gap-2">
                                        <div class="name d-flex justify-content-between">
                                            <div class="d-flex gap-2 align-items-center">
                                                <div class="person fs-5 d-flex align-items-center justify-content-center">
                                                    <i class="bi bi-person"></i>  
                                                </div>
                                                <div class="d-flex flex-column gap-2">
                                                    <span class="first fw-bold">سعید</span>
                                                    <span class="his">اسفند 1403</span>
                                                </div>
                                            </div>
                                            <div class="d-flex gap-2 align-items-center">
                                                <span><i class="bi bi-star-fill"></i></span>
                                                <span class="fs-5">3.33</span>
                                            </div>
                                        </div>
                                        <span class="nor mt-3">درکل متوسط بود </span>
                                        <div class="line"></div>
                                        <div class="answerMiz d-flex flex-column gap-3">
                                            <span class="mizban">
                                                پاسخ میزبان
                                            </span>
                                            <span class="text">
                                                با احترام شما میتونستید به مواردی همچون: تمیزی و امنیت واحد تحویل به موقع خوش برخوردی میزبان احساس آرامش و بی آزاری همسایگان رو قیدکنید! برای ما تمیزی داخل خونه هنگام تحویل مهمه ن راه پله ها
                                            </span>
                                        </div>
                                    </div>
                                </div>
                                <div @click="commentFunc" class=" d-flex gap-2 align-items-end fw-bold">
                                    <span class="did">مشاهده همه نظر ها (<span class="fs-5">16</span> مورد)</span>
                                    <span class="did"><i class="bi bi-caret-left"></i></span>
                                </div>
                                <div  v-if="comment" class="allView position-fixed  rounded-3    w-50 h-100" style="z-index: 1050; ">
                    <!-- پنل سمت راست -->
                    <div class="  d-flex flex-column  position-absolute end-0 bg-white w-100 h-100">
                        
                        <!-- هدر ثابت بالا -->
                        <div class="p-3 bg-white shadow-sm 3">
                        <div class="d-flex  gap-2 align-items-center">
                            <span @click="closeComment" class="border p-1 rounded" style="cursor: pointer;">
                            <i class="bi bi-x-lg"></i>
                            </span>
                            <span class="fw-bold ">نظرات مهمان ها </span>
                        </div>
                        </div>
                        <div class="line"></div>
                        <!-- محتوای اسکرول‌پذیر -->
                        <div class="flex-grow-1 overflow-auto px-3">
                        <div class="section py-3 border-bottom d-flex flex-column gap-3">
                            <div class="point d-flex flex-column gap-3">
                                <div class="header d-flex gap-2">
                                    <span class="star"><i class="bi bi-star-fill"></i></span>
                                    <span class="fw-bold">4.8 امتیاز </span>
                                    <span class="text">(18 مهمان )</span>
                                </div>
                                <div class="d-flex w-100 gap-3 justify-content-between">
                                    <div class="d-flex w-100 flex-column gap-3">
                                    <div class="d-flex justify-content-between align-items-center">
                                        <span>امنیت محله </span>
                                        <div class="d-flex align-items-center gap-5">
                                            <div class="line "></div>
                                        <span>4.9/5</span>
                                        </div>
                                        
                                    </div>
                                    <div class="d-flex justify-content-between">
                                        <span>پذیرش میزبان</span>
                                        <div class="d-flex align-items-center gap-5">
                                            <div class="line "></div>
                                        <span class="fw-bold fs-5">4.9/5</span>
                                        </div>
                                    </div>
                                    <div class="d-flex justify-content-between">
                                        <span>نظافت و تمیزی </span>
                                        <div class="d-flex align-items-center gap-5">
                                            <div class="line "></div>
                                        <span class="fw-bold fs-5">4.8/5</span>
                                        </div>
                                    </div>
                                    <div class="d-flex justify-content-between">
                                        <span>ارتباط با میزبان</span>
                                        <div class="d-flex align-items-center gap-5">
                                            <div class="line "></div>
                                        <span class="fw-bold fs-5">4.9/5</span>
                                        </div>
                                    </div>
                                    <div class="d-flex justify-content-between">
                                        <span>ارزش کلی اقامگاه </span>
                                        <div class="d-flex align-items-center gap-5">
                                            <div class="line "></div>
                                        <span class="fw-bold fs-5">4.6/5</span>
                                        </div>
                                    </div>
                                    <div class="d-flex justify-content-between">
                                        <span>صحت اطلاعات</span>
                                        <div class="d-flex align-items-center gap-5">
                                            <div class="line "></div>
                                        <span class="fw-bold fs-5">4.9/5</span>
                                        </div>
                                    </div>
                                </div>
                              
                                </div>
                             
                            </div>
                        </div>
                        <!-- بخش سرویس بهداشتی -->
                        <div class="py-3 border-bottom d-flex flex-column gap-3">
                            <div class="d-flex gap-3">
                                <span><img alt="نظرات" loading="lazy" width="28" height="28" decoding="async" data-nimg="1" style="color: transparent;" src="https://cdn.otaghak.com/otg-images-new/Web/Icon/general/chat.svg"></span>
                                <span class="fw-bold ">
                              نظرات 
                            </span>
                            <span class="text">(16نظر)</span>
                            </div>
                            
                            <div class="box border rounded-4 p-3 d-flex flex-column gap-2">
                                        <div class="name d-flex justify-content-between">
                                            <div class="d-flex gap-2 align-items-center">
                                                <div class="person fs-5 d-flex align-items-center justify-content-center">
                                                    <i class="bi bi-person"></i>  
                                                </div>
                                                <div class="d-flex flex-column gap-2">
                                                    <span class="first fw-bold">سعید</span>
                                                    <span class="his">اسفند 1403</span>
                                                </div>
                                            </div>
                                            <div class="d-flex gap-2 align-items-center">
                                                <span><i class="bi bi-star-fill"></i></span>
                                                <span class="fs-5">3.33</span>
                                            </div>
                                        </div>
                                        <span class="nor mt-3">درکل متوسط بود </span>
                                        <div class="line"></div>
                                        <div class="answerMiz d-flex flex-column gap-3">
                                            <span class="mizban">
                                                پاسخ میزبان
                                            </span>
                                            <span class="text">
                                                با احترام شما میتونستید به مواردی همچون: تمیزی و امنیت واحد تحویل به موقع خوش برخوردی میزبان احساس آرامش و بی آزاری همسایگان رو قیدکنید! برای ما تمیزی داخل خونه هنگام تحویل مهمه ن راه پله ها
                                            </span>
                                        </div>
                            </div>
                            <div class="box border rounded-4 p-3 d-flex flex-column gap-2">
                                <div class="name d-flex justify-content-between">
                                    <div class="d-flex gap-2 align-items-center">
                                        <div class="person fs-5 d-flex align-items-center justify-content-center">
                                            <i class="bi bi-person"></i>  
                                        </div>
                                        <div class="d-flex flex-column gap-2">
                                            <span class="first fw-bold">سعید</span>
                                            <span class="his">اسفند 1403</span>
                                        </div>
                                    </div>
                                    <div class="d-flex gap-2 align-items-center">
                                        <span><i class="bi bi-star-fill"></i></span>
                                        <span class="fs-5">3.33</span>
                                    </div>
                                </div>
                                <span class="nor mt-3">درکل متوسط بود </span>
                                <div class="line"></div>
                                <div class="answerMiz d-flex flex-column gap-3">
                                    <span class="mizban">
                                        پاسخ میزبان
                                    </span>
                                    <span class="text">
                                        با احترام شما میتونستید به مواردی همچون: تمیزی و امنیت واحد تحویل به موقع خوش برخوردی میزبان احساس آرامش و بی آزاری همسایگان رو قیدکنید! برای ما تمیزی داخل خونه هنگام تحویل مهمه ن راه پله ها
                                    </span>
                                </div>
                            </div>
                            <div class="box border rounded-4 p-3 d-flex flex-column gap-2">
                                <div class="name d-flex justify-content-between">
                                    <div class="d-flex gap-2 align-items-center">
                                        <div class="person fs-5 d-flex align-items-center justify-content-center">
                                            <i class="bi bi-person"></i>  
                                        </div>
                                        <div class="d-flex flex-column gap-2">
                                            <span class="first fw-bold">سعید</span>
                                            <span class="his">اسفند 1403</span>
                                        </div>
                                    </div>
                                    <div class="d-flex gap-2 align-items-center">
                                        <span><i class="bi bi-star-fill"></i></span>
                                        <span class="fs-5">3.33</span>
                                    </div>
                                </div>
                                <span class="nor mt-3">درکل متوسط بود </span>
                                <div class="line"></div>
                                <div class="answerMiz d-flex flex-column gap-3">
                                    <span class="mizban">
                                        پاسخ میزبان
                                    </span>
                                    <span class="text">
                                        با احترام شما میتونستید به مواردی همچون: تمیزی و امنیت واحد تحویل به موقع خوش برخوردی میزبان احساس آرامش و بی آزاری همسایگان رو قیدکنید! برای ما تمیزی داخل خونه هنگام تحویل مهمه ن راه پله ها
                                    </span>
                                </div>
                            </div>
                            <div class="box border rounded-4 p-3 d-flex flex-column gap-2">
                                <div class="name d-flex justify-content-between">
                                    <div class="d-flex gap-2 align-items-center">
                                        <div class="person fs-5 d-flex align-items-center justify-content-center">
                                            <i class="bi bi-person"></i>  
                                        </div>
                                        <div class="d-flex flex-column gap-2">
                                            <span class="first fw-bold">سعید</span>
                                            <span class="his">اسفند 1403</span>
                                        </div>
                                    </div>
                                    <div class="d-flex gap-2 align-items-center">
                                        <span><i class="bi bi-star-fill"></i></span>
                                        <span class="fs-5">3.33</span>
                                    </div>
                                </div>
                                <span class="nor mt-3">درکل متوسط بود </span>
                                <div class="line"></div>
                                <div class="answerMiz d-flex flex-column gap-3">
                                    <span class="mizban">
                                        پاسخ میزبان
                                    </span>
                                    <span class="text">
                                        با احترام شما میتونستید به مواردی همچون: تمیزی و امنیت واحد تحویل به موقع خوش برخوردی میزبان احساس آرامش و بی آزاری همسایگان رو قیدکنید! برای ما تمیزی داخل خونه هنگام تحویل مهمه ن راه پله ها
                                    </span>
                                </div>
                            </div>
                            <div class="box border rounded-4 p-3 d-flex flex-column gap-2">
                                <div class="name d-flex justify-content-between">
                                    <div class="d-flex gap-2 align-items-center">
                                        <div class="person fs-5 d-flex align-items-center justify-content-center">
                                            <i class="bi bi-person"></i>  
                                        </div>
                                        <div class="d-flex flex-column gap-2">
                                            <span class="first fw-bold">سعید</span>
                                            <span class="his">اسفند 1403</span>
                                        </div>
                                    </div>
                                    <div class="d-flex gap-2 align-items-center">
                                        <span><i class="bi bi-star-fill"></i></span>
                                        <span class="fs-5">3.33</span>
                                    </div>
                                </div>
                                <span class="nor mt-3">درکل متوسط بود </span>
                                <div class="line"></div>
                                <div class="answerMiz d-flex flex-column gap-3">
                                    <span class="mizban">
                                        پاسخ میزبان
                                    </span>
                                    <span class="text">
                                        با احترام شما میتونستید به مواردی همچون: تمیزی و امنیت واحد تحویل به موقع خوش برخوردی میزبان احساس آرامش و بی آزاری همسایگان رو قیدکنید! برای ما تمیزی داخل خونه هنگام تحویل مهمه ن راه پله ها
                                    </span>
                                </div>
                            </div>
                            <div class="box border rounded-4 p-3 d-flex flex-column gap-2">
                                <div class="name d-flex justify-content-between">
                                    <div class="d-flex gap-2 align-items-center">
                                        <div class="person fs-5 d-flex align-items-center justify-content-center">
                                            <i class="bi bi-person"></i>  
                                        </div>
                                        <div class="d-flex flex-column gap-2">
                                            <span class="first fw-bold">سعید</span>
                                            <span class="his">اسفند 1403</span>
                                        </div>
                                    </div>
                                    <div class="d-flex gap-2 align-items-center">
                                        <span><i class="bi bi-star-fill"></i></span>
                                        <span class="fs-5">3.33</span>
                                    </div>
                                </div>
                                <span class="nor mt-3">درکل متوسط بود </span>
                                <div class="line"></div>
                                <div class="answerMiz d-flex flex-column gap-3">
                                    <span class="mizban">
                                        پاسخ میزبان
                                    </span>
                                    <span class="text">
                                        با احترام شما میتونستید به مواردی همچون: تمیزی و امنیت واحد تحویل به موقع خوش برخوردی میزبان احساس آرامش و بی آزاری همسایگان رو قیدکنید! برای ما تمیزی داخل خونه هنگام تحویل مهمه ن راه پله ها
                                    </span>
                                </div>
                            </div>
                        </div>
                    
                        
                        </div>
                    
                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="line"></div>
                    <div class="prof">
                        <div class="prof-container">
                            <div class="name d-flex gap-2 mt-4">
                                <img alt="otaghak.com" loading="lazy" width="72" height="72" decoding="async" data-nimg="1" class="HostFullProfile_userImg__0sl4l image" style="color: transparent;" src="https://core.otaghak.com/api/v1/Media/images/3423955/1/1" >
                                <div class="d-flex flex-column gap-2">
                                    <span class="fw-bold first">پری رجبی</span>
                                    <span class="text">کمتر از 1 سال میزبان اتاقک </span>
                                </div>
                            </div>
                            <div class="d-flex flex-column gap-3 mt-3">
                                <div class="detail d-flex align-items-center gap-3">
                                <span><img alt="اتاقک" fetchpriority="high" width="24" height="24" decoding="async" data-nimg="1" style="color: transparent;" src="https://cdn.otaghak.com/otg-images/Web/Icon/clock-rewind-response.svg"></span>
                                <div class="d-flex flex-column gap-1">
                                    <span>زمان پاسخگویی</span>
                                    <span class="text">کمتر 7 دقیقه</span>
                                </div>
                            </div>
                            <div class="detail d-flex align-items-center gap-3">
                                <span><img alt="اتاقک" fetchpriority="high" width="24" height="24" decoding="async" data-nimg="1" style="color: transparent;" src="https://cdn.otaghak.com/otg-images/Web/Icon/circle-tick-confirm-accept.svg"></span>
                                <div class="d-flex flex-column gap-1">
                                    <span>میزان تایید رزرو </span>
                                    <span class="text">در حدود 100 درصد</span>
                                </div>
                            </div>
                                <router-link to="/profile" class="link border d-flex align-items-end" >
                                <span class="did">مشاهده پروفایل میزبان</span>
                                <span class="did " ><i class="bi bi-caret-left"></i></span>
                                </router-link>
                            
                            </div>
                            
                        </div>
                    </div>
                    <div class="line"></div>
                    <div class="other">
                        <div class="other-container">
                            <div class="d-flex flex-column">
                                <div class="d-flex gap-3">
                                <span>سایر اقامتگاه های پری رجبی </span>
                                <span class="text">(1 اقامتگاه)</span>
                            </div>
                            <rooms/>

                            </div>
                            <div class="line"></div>
                            <div class="other-like d-flex flex-column gap-4">
                                <span>سایر اقامتگاه های مشابه در منطقه </span>
                                <rooms/>
                            </div>
                        </div>
                    </div>
            </div>
            <div class="left  col-4 p-4">
                <div class="contain border rounded-3 p-2 d-flex flex-column gap-4">
                <div class="price d-flex  justify-content-between">
                    <div class="border d-flex align-items-center gap-2">
                        <div class=" d-flex align-items-center justify-content-center gap-1 bg-danger rounded-3 p-1 fs-5 text-white">
                            <span>5</span>
                            <span><i class="bi bi-percent"></i></span>
                        </div>
                        <span class="under fs-5 d-flex align-items-center"> 2/100/000</span>
                  
                    </div>
                    <div class="border fs-5">
                        <span>هر شب از </span>
                        <span>1/995/000</span>
                        <span>تومان</span>
                    </div>
                  
                </div>
                <div class="history d-flex gap-3 position-relative">
                    <div @click="calendarFunc" class="open d-flex p-2 gap-2 w-50 border rounded-3 justify-content-end">
                            <span>تاریخ ورود</span>
                            <span><i class="bi bi-calendar-plus-fill"></i></span>
                    </div>
                    <div @click="calendarFunc" class="close d-flex p-2  gap-2 w-50 border rounded-3 justify-content-end">
                        <span>
                            تاریخ خروج
                        </span>
                        <span>
                            <i class="bi bi-calendar-x-fill"></i>
                        </span>
                    </div>
                        <div v-if="calendar" id="his" class="history-calender bg-white position-absolute rounded-3 ">
                            <div class="history-calender-container d-flex flex-column p-2 gap-2">

                            <div class="d-flex justify-content-end align-items-center  gap-2 p-2">
                                    <div class="clos p-2 d-flex   gap-2 w-50 border rounded-3 justify-content-end">
                                    <span>
                                        تاریخ خروج
                                    </span>
                                    <span>
                                        <i class="bi bi-calendar-x-fill"></i>
                                    </span>
                                 </div>
                                <div class="ope p-2 d-flex  gap-2 w-50 border rounded-3 justify-content-end">
                            <span>تاریخ ورود</span>
                            <span><i class="bi bi-calendar-plus-fill"></i></span>
                                </div>
                                <span class=" travel text-end ">تاریخ سفر </span>
                                </div>
                                <div class="month">
                                    <div class="month-container d-flex w-100 ">
                                        <div v-if="next" class="khordad d-flex flex-column w-50 gap-2 align-items-end">
                                            <div class="d-flex gap-2 w-100 align-items-center">
                                                <div v-if="!next" class="d-flex w-25">
                                                 
                                                <div  class="border">
                                                    <i class="bi bi-caret-left"></i>
                                                </div>
                                            
                                                </div>
                                                <div class="d-flex  gap-2 w-75 justify-content-center align-items-center fw-bold">
                                                <span class="fs-5">1404</span>
                                                <span>خرداد</span>

                                                </div>
                                                <div v-if="next" class="d-flex w-25">
                                                    <i class="bi bi-caret-right"></i>
                                                </div>
                                                
                                            </div>
                                            <div class="days d-flex gap-2 justify-content-center w-100">
                                                <span> جمعه</span>
                                                <span>پنج شنبه</span>
                                                <span>چهارشنبه</span>
                                                <span> سه شنبه</span>
                                                <span>دوشنبه</span>
                                                <span>یک شنبه</span>
                                                <span>شنبه</span>
                                            </div>

                                            <div  class=" day d-flex flex-row-reverse justify-content-end   w-100   row">
                                                    <div class=" d-flex flex-column align-items-start w-100 ">
                                                        <div class="d-flex flex-column align-items-center ">
                                                            <span>1</span>
                                                        <span>2/500 </span>
                                                        </div>
                                                        
                                                    </div>
                                                <div  class=" items gap-2 row d-flex flex-row-reverse   w-100 ">
                                                
                                                <div v-for="(item, index) in number" :key="index"
                                                class="item    d-flex flex-column  align-items-center "
                                                 :class="{am : ((item)%7)==1, ab: (item<=16)}" >
                                                 <div v-if="item<=31">
                                                 {{ item }}
                                                 <div class="" v-if="item>15">
                                                   
                                                   2/500
                                         
                                               </div>
                                                 </div>
                                                 

                                                </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="ordi d-flex flex-column w-50 gap-2 align-items-end">
                                            <div class="d-flex gap-2 w-100 align-items-center">
                                                <div class="d-flex w-25">
                                                <div v-if="!next" @click="nextfunc">
                                                    <i class="bi bi-caret-left"></i>
                                                </div>
                                               
                                                </div>
                                                <div class="d-flex  gap-2 w-75 justify-content-start align-items-center fw-bold">
                                                <span class="fs-5">1404</span>
                                                <span>اردیبهشت</span>

                                                </div>
                                           
                                                <div v-if="next">
                                                    <i class="bi bi-caret-right"></i>
                                                </div>
                                            </div>
                                            <div class="days d-flex gap-2 justify-content-center w-100">
                                                <span> جمعه</span>
                                                <span>پنج شنبه</span>
                                                <span>چهارشنبه</span>
                                                <span> سه شنبه</span>
                                                <span>دوشنبه</span>
                                                <span>یک شنبه</span>
                                                <span>شنبه</span>
                                            </div>

                                            <div  class=" day d-flex flex-row-reverse justify-content-end   w-100   row">
                                                    <div class=" d-flex flex-column align-items-start w-100 ">
                                                        <div class="d-flex flex-column align-items-center ">
                                                            <span>1</span>
                                                        <span>2/500 </span>
                                                        </div>
                                                        
                                                    </div>
                                                <div  class=" items gap-2 row d-flex flex-row-reverse   w-100 ">
                                                
                                                <div v-for="(item, index) in number" :key="index"
                                                class="item    d-flex flex-column  align-items-center "
                                                 :class="{am : ((item)%7)==1, ab: (item<=16)}" >
                                                 <div v-if="item<=31">
                                                 {{ item }}
                                                 <div class="" v-if="item>15">
                                                   
                                                   2/500
                                         
                                               </div>
                                                 </div>
                                                 

                                                </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div v-if="!next" class="farvardin d-flex flex-column w-50 gap-2 align-items-end">
                                            <div class="d-flex gap-2 w-100 align-items-center">
                                                <div class="d-flex  ms-5 gap-2 w-75 justify-content-center align-items-center fw-bold">
                                                <span class="fs-5">1404</span>
                                                <span>فروردین</span>

                                                </div>
                                                <div class="d-flex w-25">
                                                <span>
                                                    <i class="bi bi-caret-right"></i>
                                                </span>
                                                </div>
                                                
                                            </div>
                                            <div class="days d-flex gap-2 justify-content-center w-100">
                                                <span> جمعه</span>
                                                <span>پنج شنبه</span>
                                                <span>چهارشنبه</span>
                                                <span> سه شنبه</span>
                                                <span>دوشنبه</span>
                                                <span>یک شنبه</span>
                                                <span>شنبه</span>
                                            </div>

                                            <div  class=" day d-flex flex-row-reverse justify-content-end   w-100   row">
                                                    <div class=" d-flex flex-column align-items-start w-100 ">
                                                        <div class="d-flex flex-column align-items-center ">
                                                            <span>1</span>
                                                        <span>2/500 </span>
                                                        </div>
                                                        
                                                    </div>
                                                <div  class=" items gap-2 row d-flex flex-row-reverse   w-100 ">
                                                
                                                <div v-for="(item, index) in number" :key="index"
                                                class="item   d-flex flex-column  align-items-center "
                                                 :class="{am : ((item)%7)==1, ab: (item<=16)}" >
                                                 <div v-if="item<=31">
                                                 {{ item }}
                                                 <div class="" v-if="item>15">
                                                   
                                                   2/500
                                         
                                               </div>
                                                 </div>
                                                 

                                                </div>
                                                </div>
                                            </div>
                                        </div>
                                      
                                     
                                    </div>
                                </div>
                                <div class="line w-100">

                                </div>
                                <div class="accept">
                                    <div class="d-flex accept-container w-100">
                                        <div class="left w-50">
                                            <button class="but rounded-3 text-white d-flex justify-content-center align-items-center">
                                                تایید تاریخ 
                                            </button>
                                       
                                        </div>
                                        <div class="right w-50 d-flex justify-content-end  align-items-center">
                                            <div class="guid d-flex gap-2 align-items-center ">
                                                <span>راهنمای تقویم</span>
                                                <span><i class="bi bi-question-circle"></i></span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                           
                        </div>
                </div>
                <div class="number">
                    <div class="number-container d-flex flex-column gap-2   "
                    @click="clickNumber"
                    >
                        <div class="d-flex justify-content-between w-100 border rounded-3 p-3">
                        <div class="icon">
                            <i class="bi bi-caret-down"></i>
                        </div>
                        <div class="fs-6 d-flex gap-2">
                            <span>تعداد نفرات را انتخاب کنید</span>
                            <span><i class="bi bi-person"></i></span>

                        </div>
                         </div>
                         <div v-if="cont" class="d-flex flex-column gap-2 align-items-end border border-primary w-100 rounded-3">
                            <span>تعداد نفرات را انتخاب کنید</span>
                            <span>1 نفر</span>
                            <span>2 نفر </span>
                         </div>
                    </div>
                </div>
                <div class="text d-flex justify-content-end mt-3">
                <span>کودکان تا زیر 3 سال در صورتحساب لحاظ نمی گردند.</span>

                </div>
                <div class="line mt-3">
                </div>
                <div class="check d-flex gap-2 justify-content-end">
                    <span>رزرو برای دیگری </span>
                    <input type="checkbox" class="checkBox">

                </div>
                <div class="line ">
                </div>
                <div class="choice">
                    <div class="choice-container w-100  d-flex justify-content-center align-items-center p-3 rounded-3">
                        <span class="text-white fw-bold ">انتخاب تاریخ </span>
                    </div>
                </div>
                <div class="message w-100 d-flex justify-content-end align-items-center gap-2">
                    <span class=" message-text text-end">
                        پس از ثبت درخواست می توانید با میزبان خود مستقیما گفتگوی آنلاین داشته باشید
                    </span>
                    <span>
                        <i class="bi bi-chat-left-dots"></i>
                    </span>
                </div>
                </div>
             
            </div>
          
        </div>
    </div>
    <Footer />

  </template>
  
<script setup>
  import Header from './header.vue';
  import Footer from './footer.vue';
  import rooms from './rooms.vue'
  import { ref,watch } from 'vue';
  const items = ['تصاویر', 'مشخصات', 'موقعیت', 'تقویم', 'قوانین', 'نظرات'];
  const activeIndex = ref(null); // ذخیره اندیس متن فعال
  const tru=ref( false)
  const next = ref(false)
  const calendar = ref( false )
  const vie=ref(false)
  const refahi= ref( false)
  const did= ref( false)
  const comment= ref( false)
  const closeComment=()=>{
    comment.value=false
  }
  const commentFunc =()=>{
    comment.value=true
  }
  const closeDid = ()=>{ 
    did.value= false
  }
  const didFunc=()=>{ 
    did.value=true
  }
 const allView =()=>{ 
    vie.value=true
    // document.body.style.overflowY='hidden'
 }
 
 const refah =() => { 
    refahi.value=true
 }
 const closer = ()=>{ 
    refahi.value=false
 }
//  watch(vie, (val) => {
//   document.body.style.overflow = val ? 'hidden' : 'auto';
// });
 const closeView =()=>{
    vie.value = false
    // document.body.style.overflowY='visible'
   
    
    
}

  const not=()=> { 
    calendar.value=false
}
  const calendarFunc=()=> { 
    calendar.value = true
  }
 
  // وقتی روی یکی از متن‌ها کلیک شد
  const handleClick = (index) => {
    activeIndex.value = index;
    tru.value=true
console.log(tru.value);

  };
  const perFunct = ()=>{
    next.value=false
  }
  const nextfunc =() =>{ 
    next.value= true
  }
  let number =ref([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16
            ,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31])
  let cont =ref(false)
  function clickNumber() { 
    cont.value= !cont.value
    console.log(cont.value);

  }

  document.addEventListener('DOMContentLoaded', function () {
    const map = L.map('map').setView([35.6892, 51.3890], 13); // مختصات تهران
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);

    L.marker([35.6892, 51.3890]).addTo(map)
      .bindPopup('موقعیت تقریبی اقامتگاه')
      .openPopup();
  });
  </script>
  
  <style scoped>
  @import url('../assets/header.css');
  @import url('../assets/room.css');
  

  </style>