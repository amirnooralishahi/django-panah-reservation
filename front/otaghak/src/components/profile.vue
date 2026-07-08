<template>
  <Header />
  <div class="container py-5 mt-3" dir="rtl">
    <div v-if="message" class="alert alert-success alert-dismissible fade show">
      {{ message }}
      <button type="button" class="btn-close" @click="message = ''"></button>
    </div>
    <div v-if="error" class="alert alert-danger alert-dismissible fade show">
      {{ error }}

      <button type="button" class="btn-close" @click="error = ''"></button>
    </div>
    <div class="mb-3">
      <router-link to="/" class="btn btn-outline-secondary"
        >بازگشت به صفحه اصلی</router-link
      >
    </div>
    <div class="card shadow-sm border-0">
      <div class="card-body ">
        <div
          class="d-flex flex-column flex-md-row justify-content-between align-items-start gap-3 mb-4"
        >
          <div>
            <h2 class="fw-bold mb-2">
              {{ isHost ? "پروفایل میزبان" : "پروفایل کاربر" }}
            </h2>
            <p class="text-muted mb-0">
              {{
                isHost
                  ? "اطلاعات میزبان و مدیریت اقامتگاه‌ها"
                  : "اطلاعات شخصی و رزروهای شما"
              }}
            </p>
          </div>
          <span
            class="badge rounded-pill"
            :class="isHost ? 'bg-success' : 'bg-primary'"
            >{{ isHost ? "میزبان" : "کاربر عادی" }}</span
          >
        </div>

        <div class="row g-4">
          <div class="col-lg-8">
            <div class="card border-0 bg-light">
              <div class="card-body">
                <h5 class="fw-bold mb-3">اطلاعات پروفایل</h5>

                <div v-if="error" class="alert alert-warning">{{ error }}</div>
                <div v-else>
                  <div class="row g-3">
                    <div class="col-md-6">
                      <label class="form-label">نام کاربری</label>
                      <input
                        v-model="profile.username"
                        class="form-control"
                        type="text"
                        disabled
                      />
                    </div>
                    <div class="col-md-6">
                      <label class="form-label">کد ملی</label>
                      <input
                        v-model="profile.NationalCode"
                        class="form-control"
                        type="text"
                        disabled
                      />
                    </div>
                    <div class="col-md-6">
                      <label class="form-label">ایمیل</label>
                      <input
                        v-model="profile.email"
                        class="form-control"
                        type="email"
                      />
                    </div>
                    <div class="col-md-6">
                      <label class="form-label">شماره همراه</label>
                      <input
                        v-model="profile.phone"
                        class="form-control"
                        type="text"
                      />
                    </div>
                    <div class="col-md-6">
                      <label class="form-label">شغل</label>
                      <input
                        v-model="profile.Job_title"
                        class="form-control"
                        type="text"
                      />
                    </div>
                    <div class="col-md-6">
                      <label class="form-label">شناسه پروفایل</label>
                      <input
                        v-model="profile.slug"
                        class="form-control"
                        type="text"
                        disabled
                      />
                    </div>
                  </div>

                  <button class="btn btn-success mt-4" @click="saveProfile">
                    ذخیره تغییرات
                  </button>
                  
                </div>
              </div>
            </div>
          </div>

          <div class="col-lg-4">
            <div class="card border-0 bg-dark text-white">
              <div class="card-body">
                <h5 class="fw-bold mb-3">نمای کلی</h5>
                <ul class="list-unstyled mb-0">
                  <li class="mb-2">
                    نام کاربری: {{ profile.username || "---" }}
                  </li>
                  <li class="mb-2">ایمیل: {{ profile.email || "---" }}</li>
                  <li>شغل: {{ profile.Job_title || "---" }}</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-if="isHost">
      <div v-if="myRooms.length">
        <h3>اقامتگاه های من</h3>

        <div
          v-for="room in myRooms"
          :key="room.id"
          class="card my-3 shadow"
        >
          <img
            v-if="room.images.length"
            :src="'http://127.0.0.1:8000' + room.images[0].image"
            class="card-img-top"
            style="height: 220px; object-fit: cover"
          />

          <div class="card-body">
            <template v-if="editingRoomId !== room.id">
              <h4>{{ room.Dormitory }}</h4>

              <p>شهر: {{ room.city }}</p>

              <p>قیمت: {{ room.price }}</p>

              <button class="btn btn-warning me-2" @click="startEditRoom(room)">
                ویرایش
              </button>

              <button class="btn btn-danger" @click="removeRoom(room.id)">
                حذف
              </button>
            </template>

            <template v-else>
              <div class="mb-2">
                <input
                  class="form-control"
                  v-model="roomEdits.Dormitory"
                  placeholder="نام اقامتگاه"
                />
              </div>

              <div class="mb-2">
                <input
                  class="form-control"
                  v-model="roomEdits.city"
                  placeholder="شهر"
                />
              </div>

              <div class="mb-2">
                <input
                  class="form-control"
                  v-model="roomEdits.location"
                  placeholder="آدرس"
                />
              </div>

              <div class="mb-2">
                <input
                  class="form-control"
                  v-model="roomEdits.price"
                  placeholder="قیمت"
                />
              </div>

              <button class="btn btn-success me-2" @click="saveRoom(room.id)">
                ذخیره
              </button>

              <button class="btn btn-secondary" @click="cancelEditRoom">
                انصراف
              </button>
            </template>
          </div>
        </div>
      </div>

      <div v-else class="alert alert-info mt-3">
        هنوز هیچ اقامتگاهی ثبت نکرده اید
      </div>
    </div>
    <div v-else>
      <h3 class="mt-5">رزروهای من</h3>

      <div v-for="item in myReservations" :key="item.id" class="room-card">
        <img
          v-if="item.image"
          :src="'http://127.0.0.1:8000' + item.image"
          width="250"
        />

        <h4>{{ item.room_name }}</h4>

        <p>{{ item.city }}</p>

        <p>
          ورود:
          {{ item.ReservDate }}
        </p>

        <p>
          خروج:
          {{ item.DeliveryDate }}
        </p>
      </div>
      <div v-if="!myReservations.length" class="alert alert-info mt-3">
        هنوز رزروی ثبت نکرده اید
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from "vue";
import Header from "./header.vue";
import {
  fetchRooms,
  fetchUserProfile,
  updateRoom,
  updateUserProfile,
  fetchMyRooms,
  fetchMyReservations,
  deleteRoom,
} from "@/services/api";
const myRooms = ref([]);
const myReservations = ref([]);
const isHost = computed(
  () => localStorage.getItem("user_role") === "home_owner",
);
const message = ref("");
const error = ref("");
const profile = ref({
  username: "",
  slug: "",
  email: "",
  phone: "",
  NationalCode: "",
  Job_title: "",
  id: null,
});
// const hostRooms = ref([]);
const editingRoomId = ref(null);
const roomEdits = ref({});


async function loadProfile() {
  message.value = "";
  error.value = "";

  if (!localStorage.getItem("access_token")) {
    error.value = "برای دسترسی به پروفایل ابتدا وارد شوید.";
    return;
  }

  try {
    const data = await fetchUserProfile();
    profile.value = {
      username: localStorage.getItem("user_name") || "",
      slug: data.slug || "",
      email: data.email || "",
      phone: data.phone || "",
      NationalCode: data.NationalCode || "",
      Job_title: data.Job_title || "",
      id: data.id || null,
    };

    if (profile.value.id) {
      localStorage.setItem("profile_id", profile.value.id);
    }

    
  } catch (err) {
    error.value = err.message || "بارگذاری اطلاعات پروفایل با خطا مواجه شد.";
  }
}

async function saveProfile() {
  message.value = "";
  error.value = "";
  try {
    const updateData = {
      email: profile.value.email,
      phone: profile.value.phone,
      Job_title: profile.value.Job_title,
    };
    const result = await updateUserProfile(updateData);
    profile.value = {
      ...profile.value,
      email: result.email || profile.value.email,
      phone: result.phone || profile.value.phone,
      Job_title: result.Job_title || profile.value.Job_title,
    };
    message.value = "تغییرات با موفقیت ذخیره شد.";
  } catch (err) {
    error.value = err.message || "ذخیره‌سازی با خطا مواجه شد.";
  }
}

function startEditRoom(room) {
try{
  editingRoomId.value = room.id;

  roomEdits.value = {
    location: room.location,

    city: room.city,

    price: room.price,

    Dormitory: room.Dormitory,

    building_Information: room.building_Information,

    Bed_Service: room.Bed_Service,

    Toilet_Bathroom: room.Toilet_Bathroom,

    Accommodation_cap: room.Accommodation_cap,

    Perspective: room.Perspective,

    Internal_Faclities: room.Internal_Faclities,

    Additional_details: room.Additional_details,

    time_reserve: room.time_reserve,
  };
}catch{ 
  error.value="انجام نشد"
}
  
}

function cancelEditRoom() {
  editingRoomId.value = null;
  roomEdits.value = {};
}

async function saveRoom(id) {
  try {
    const updated = await updateRoom(id, roomEdits.value);

    const index = myRooms.value.findIndex((room) => room.id === id);

    if (index !== -1) {
      myRooms.value[index] = {
        ...myRooms.value[index],
        ...updated,
      };
    }

    editingRoomId.value = null;

    roomEdits.value = {};

    message.value = "اقامتگاه با موفقیت ویرایش شد";
    error.value = "";
  } catch (err) {
    console.log(err);

    error.value = "ویرایش انجام نشد";
    message.value = "";
  }
}

onMounted(async () => {
  await loadProfile();
  const role = localStorage.getItem("user_role");

  if (role === "home_owner") {
    const rooms = await fetchMyRooms();
    myRooms.value = rooms;
  } else {
    myReservations.value = await fetchMyReservations();
  }
});
async function removeRoom(id) {
  if (!confirm("آیا مطمئن هستید؟")) return;
try{
  await deleteRoom(id);

  myRooms.value = myRooms.value.filter((room) => room.id !== id);
  message.value = "اقامتگاه حذف شد";
  
}catch{ 
  error.value = "حذف انجام نشد ";
}
  
}
</script>

<style scoped>
.card {
  border-radius: 1rem;
}
</style>
