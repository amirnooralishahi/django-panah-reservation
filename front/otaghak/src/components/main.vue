<template>
  <Header />
  <div class="search mb-5">
    <div
      class="search-contain w-100 gap-5 d-flex justify-content-center align-items-center"
    >
      <div class="center d-flex flex-column align-items-center gap-3 ">
        <span class="vila text-white fw-bold rounded-3 p-2 text-center"
          >اجاره ویلا و سوئیت در سراسر ایران
        </span>

        <div class="box d-flex rounded-4 px-2 gap-1">
          <div class="d-flex align-items-center">
            <button @click="handleSearch" class="box-search p-2 px-3 rounded-3">
              <i class="bi bi-search text-white"></i>
            </button>
          </div>

          <div
            class="text d-flex w-100 justify-content-center align-items-center"
          >
            <input
              v-model="searchQuery"
              @keydown.enter="handleSearch"
              type="text"
              placeholder="جستجوی شهر و استان"
              class="city h-75"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
  <Destination />
  <Speed />

  <div class="container my-5">
    <div class="d-flex justify-content-between align-items-center mb-3">
      <h3 class="fw-bold text-end">اقامتگاه‌های پیشنهادی</h3>
      <router-link to="/room" class="text-success fw-bold">مشاهده همه</router-link>
    </div>

    <div v-if="loadingRooms" class="text-center py-4">در حال بارگذاری اقامتگاه‌ها…</div>
    <div v-else-if="roomsError" class="alert alert-danger">{{ roomsError }}</div>
    <div v-else class="row g-4">
      <div v-for="(room, index) in rooms.slice(0, 6)" :key="room.id ?? room.Dormitory ?? index" class="col-12 col-md-6 col-lg-4">
        <item-room :room="room" :image="previewImages[index % previewImages.length]" />
      </div>
    </div>
  </div>

  <div class="mizban w-100 mt-4 d-flex justify-content-center">
    <div class="mizban-container">
      <div class="image d-flex justify-content-center">
        <img
          src="./../../New_folder/mizban.webp"
          alt=""
          class="img rounded-3"
        />
      </div>
    </div>
  </div>
  <div class="comment mt-5">
    <div class="comment-container d-flex justify-content-center">
      <div class="swiper-container">
        <swiper
          :modules="[Autoplay]"
          :slides-per-view="3"
          :space-between="10"
          :loop="true"
          :autoplay="{ delay: 4000, disableOnInteraction: false }"
          :effect="'coverflow'"
          :coverflowEffect="{
            rotate: 0,
            stretch: 50,
            depth: 100,
            modifier: 3,
            slideShadows: false,
          }"
          @swiper="onSwiperInit"
          @slideChange="onSlideChange"
          :centeredSlides="true"
          class="custom-swiper p-4 d-flex flex-column gap-3"
        >
          <swiper-slide
            class="com d-flex flex-column align-items-center justify-content-start gap-4 p-5"
          >
            <span>اکرم </span>
            <span class="text-end"
              >جای دلنشینی بود و ویوی زیبایی داشت و پارکینگ و همه امکانات هم مثل
              همون چیزی که داخل سایت دیده بودیم بود کاملا و پک های بهداشتی که
              پناه داده بود بهمون هم خیلی مفید بود و اقاامت به یادماندنی و
              مناسبی بود
            </span>
          </swiper-slide>
          <swiper-slide
            class="com d-flex flex-column align-items-center justify-content-start gap-4 p-5"
          >
            <span>شایان </span>
            <span class="text-end">
              سلام وقت بخیر. اقامتگاه بسیار عالی از همه لحاظ ( نظافت،امکانات
              رفاهی منظره) فاصله کم با دریا و جنگل تشکر ویژه دارم از جناب شعبانی
              عزیز بابت میزبانی عالیشون به ما که خیلی خوش گذشت پیشنهاد میکنم
              حتما امتحان کنید تشکر از عوامل پناه
            </span>
          </swiper-slide>
          <swiper-slide
            class="com d-flex flex-column align-items-center justify-content-start gap-4 p-5"
          >
            <span>امیر </span>
            <span class="text-end">
              به لحاظ موقعیت مکانی و دسترسی فوقالعاده است و به معنی واقعی کلمه
              چسبیده به مرکز خرید جواهیر و مترو شیشلی هست و منطقه خوب و امنی
              هست. کاملا مقل عکسهایی بود که تو پناه گذاشته و تمیز و مرتب ،
              ارتباط میزبان خیلی خوب بود
            </span>
          </swiper-slide>
          <swiper-slide
            class="com d-flex flex-column align-items-center justify-content-start gap-4 p-5"
          >
            <span>اکرم </span>
            <span class="text-end"
              >جای دلنشینی بود و ویوی زیبایی داشت و پارکینگ و همه امکانات هم مثل
              همون چیزی که داخل سایت دیده بودیم بود کاملا و پک های بهداشتی که
              پناه داده بود بهمون هم خیلی مفید بود و اقاامت به یادماندنی و
              مناسبی بود
            </span>
          </swiper-slide>
          <swiper-slide
            class="com d-flex flex-column align-items-center justify-content-start gap-4 p-5"
          >
            <span>شایان </span>
            <span class="text-end">
              سلام وقت بخیر. اقامتگاه بسیار عالی از همه لحاظ ( نظافت،امکانات
              رفاهی منظره) فاصله کم با دریا و جنگل تشکر ویژه دارم از جناب شعبانی
              عزیز بابت میزبانی عالیشون به ما که خیلی خوش گذشت پیشنهاد میکنم
              حتما امتحان کنید تشکر از عوامل پناه
            </span>
          </swiper-slide>
          <swiper-slide
            class="com d-flex flex-column align-items-center justify-content-start gap-4 p-5"
          >
            <span>امیر </span>
            <span class="text-end">
              به لحاظ موقعیت مکانی و دسترسی فوقالعاده است و به معنی واقعی کلمه
              چسبیده به مرکز خرید جواهیر و مترو شیشلی هست و منطقه خوب و امنی
              هست. کاملا مقل عکسهایی بود که تو پناه گذاشته و تمیز و مرتب ،
              ارتباط میزبان خیلی خوب بود
            </span>
          </swiper-slide>
          <div class="button d-flex w-100 justify-content-center gap-4 mt-4">
            <button
              v-for="(btn, index) in 6"
              :key="'btn-' + index"
              :class="['custom-prevv', { 'active-btn': index === activeIndex }]"
            ></button>
          </div>
        </swiper>
      </div>
    </div>
  </div>
  <Destination />
  <div class="travel">
    <div class="travel-container d-flex justify-content-center">
      <div class="d-flex flex-column text">
        <div class="d-flex flex-column align-items-end gap-2">
          <span class="text-end fw-bold fs-5"
            >سفر با پناه، آغاز یک تجربه فراموش نشدنی
          </span>
          <span class="matn text-end">
            در این روزها، زمانی که آرامش و امنیت برای همه ما اهمیت بیشتری پیدا
            کرده، ما تلاش می‌کنیم تا مسیرهای شما را ساده‌تر و دلپذیرتر کنیم. از
            لحظه‌ی انتخاب مقصد تا رسیدن به آن، پناه کنار شماست تا با خیالی
            آسوده، سفر خود را آغاز کنید. ما به جزئیات توجه می‌کنیم، از نیازهای
            شما غافل نمی‌شویم و سعی می‌کنیم هر قدم از سفر، همراهی مطمئن و صمیمی
            برایتان باشد. چرا که سفر فقط رفتن به جایی دیگر نیست؛ سفر تجربه‌ای از
            آرامش، اعتماد و خاطراتی است که در دل می‌مانند. با پناه، هر سفر
            می‌تواند از یک مسیر ساده، به یک خاطره‌ی ماندگار تبدیل شود. ما برای
            شما فقط یک سرویس نیستیم؛ ما همراهی هستیم که در کنار شما، سفرتان را
            بهتر و دلسوزانه‌تر می‌سازیم. اگر بخواهی، می‌توانم همین
          </span>
          <span class="matn text-end fw-bold">
      پناه در لحظه ها و ثانیه های شرایط سخت کشور عزیزمون در کنار شماست. 
          </span>
        </div>

        <h5 @click="retuer" class="more text-end">
          <i class="bi bi-caret-down-fill"></i> نمایش بیشتر
        </h5>
        <div v-if="click" class="d-flex flex-column align-items-end gap-3">
          <span class="matn text-end"
            >سفر با پناه، شروعی متفاوت برای لحظات خاص است. در این مسیر، ما فقط
            به دنبال ارائه‌ی خدمات نیستیم؛ ما می‌خواهیم شما را در تجربه‌ای
            همراهی کنیم که پر از آرامش، اعتماد و دقت باشد. از انتخاب مقصد گرفته
            تا لحظه‌های واپسین سفر، پناه کنار شماست تا با خیال راحت، از هر لحظه
            لذت ببرید. ما می‌دانیم که سفر، فقط یک حرکت فیزیکی نیست؛ سفر، حال و
            هوای قلبی، خاطراتی ماندگار و لحظاتی است که همیشه در یاد می‌ماند. با
            پناه، می‌توانید مطمئن باشید که در کنار شما هستیم تا این تجربه،
            شیرین‌تر و ارزشمندتر شود.</span
          >

          <h5 @click="retuer" class="more d-flex gap-2 justify-content-center">
            <i class="bi bi-caret-up-fill"></i> نمایش کمتر
          </h5>
        </div>
      </div>
    </div>
  </div>
  <!-- <div class="tag mt-4">
        <div class="tag-container d-flex flex-column align-items-center gap-2">
            <div class="row  gap-1 justify-content-end">
                <div class="col-auto border rounded-4  text-center">اجاره ویلا استخردار فیروزکوه </div>
                <div class="col-auto border rounded-4  text-center">اجاره ویلا استخردار شهریار</div>
                <div class="col-auto border rounded-4  text-center">اجاره ویلا استخردار در کردان</div>

                <div class="col-auto border rounded-4  text-center">اجاره ویلا برای مهمانی در لواسان</div>
                <div class="col-auto border rounded-4  text-center">اجاره ویلا شهریار برای تولد</div>

                <div class="col-auto border rounded-4  text-center">اجاره ویلا در کردان برای مهمانی</div>

            </div>
            <div class="row  gap-1 justify-content-end">
                <div class="col-auto border rounded-4 text-center">اجاره ویلا استخردار در کرج  </div>
                <div class="col-auto border rounded-4 text-center">اجاره ویلا استخردار در رودهن</div>
                <div class="col-auto border rounded-4 text-center">اجاره ویلا اتخردار در هشتگرد</div>

                <div class="col-auto border rounded-4 text-center">اجاره ویلا استخردار در طالقان</div>
                <div class="col-auto border rounded-4 text-center">اجاره ویلا استخردار در لواسان</div>

                <div class="col-auto border rounded-4 text-center">اجاره ویلا در فشم استخردار </div>

            </div>
          
            <div class="row  gap-1 justify-content-end">
                <div class="col-auto border rounded-4  text-center">اجاره ویلا استخردار در فومن  </div>
                <div class="col-auto border rounded-4  text-center">اجاره ویلا استخردار رشت</div>
                <div class="col-auto border rounded-4  text-center">اجاره ویلا استخردار چالوس</div>

                <div class="col-auto border rounded-4  text-center">اجاره ویلا استخردار رامسر</div>
                <div class="col-auto border rounded-4  d-flex align-items-center justify-content-center">اجاره ویلا استخردار نوشهر </div>

                <div class="col-auto border rounded-4  text-center">اجاره ویلا استخردار در دماوند</div>
          
            </div>
            <div class="row  gap-1 justify-content-end">
                <div class="col-auto border rounded-4  text-center">اجاره کلبه جنگلی در رشت </div>
                <div class="col-auto border rounded-4  text-center">اجاره کلبه چوبی فیروزکوه</div>

                <div class="col-auto border rounded-4  text-center">اجاره کلبه چوبی در لواسان</div>
                <div class="col-auto border rounded-4  text-center">اجاره کلبه چوبی در شهریار </div>

                <div class="col-auto border rounded-4  text-center">اجاره کلبه چوبی در کردان</div>

                <div class="col-auto border rounded-4  text-center">اجاره ویلا استخردار در متل قو</div>

            </div>
           
            <div class="row gap-1  justify-content-end">
                <div class="col-auto border rounded-4 text-center">اجاره کلبه جنگلی در متل قو  </div>
                <div class="col-auto border rounded-4 text-center">اجاره کلبه جنگلی در فومن </div>

                <div class="col-auto border rounded-4 text-center">کلبه جنگلی نور </div>
                <div class="col-auto border rounded-4 text-center">اجاره کلبه جنگلی سوادکوه</div>

                <div class="col-auto border rounded-4 text-center">اجاره کلبه جنگلی شیرگاه</div>

                <div class="col-auto border rounded-4 text-center">اجاره کلبه ماسال</div>

            </div>
           
        </div>
    </div> -->
  <Footer />
</template>

<script setup>
import { Swiper, SwiperSlide } from "swiper/vue";
import { Navigation, Autoplay } from "swiper/modules";
import "swiper/css";
import "swiper/css/navigation";
import itemRoom from "./itemRoom.vue";
import { ref, onMounted, watch } from "vue";
import { useRoute, useRouter } from 'vue-router'
import Destination from "./destination.vue";
import Speed from "./speed.vue";
import Header from "./header.vue";
import Footer from "./footer.vue";
import { fetchRooms } from "@/services/api";
import roomImage1 from "../../New_folder/a.webp";
import roomImage2 from "../../New_folder/b.webp";
import roomImage3 from "../../New_folder/c.webp";
import roomImage4 from "../../New_folder/d.webp";
import roomImage5 from "../../New_folder/e.webp";
import roomImage6 from "../../New_folder/f.webp";

const activeIndex = ref(0);
let click = ref(false);
const rooms = ref([]);
const loadingRooms = ref(true);
const roomsError = ref("");
const searchQuery = ref("");
const route = useRoute()
const router = useRouter()
const previewImages = [roomImage1, roomImage2, roomImage3, roomImage4, roomImage5, roomImage6];

function retuer() {
  click.value = !click.value;
}

async function loadRooms(search = "") {
  loadingRooms.value = true;
  roomsError.value = "";
  try {
    const data = await fetchRooms(search);
    rooms.value = Array.isArray(data) ? data : data?.results || [];
  } catch (error) {
    roomsError.value = error.message || "بارگذاری اقامتگاه‌ها با خطا مواجه شد.";
    rooms.value = [];
  } finally {
    loadingRooms.value = false;
  }
}

async function handleSearch() {
  // navigate to results page with query so the rooms view shows filtered results
  const q = searchQuery.value.trim()
  await router.push({ path: '/room', query: q ? { search: q } : {} })
}

// load based on route query
watch(() => route.query.search, (s) => {
  const q = s || ''
  searchQuery.value = q
  loadRooms(q)
}, { immediate: true })

onMounted(async () => {
  const q = route.query.search || ''
  searchQuery.value = q
  await loadRooms(q)
});

const onSwiperInit = (swiper) => {
  activeIndex.value = swiper.realIndex;
};

const onSlideChange = (swiper) => {
  activeIndex.value = swiper.realIndex;
};
</script>

<style>
@import "../assets/header.css";
</style>
