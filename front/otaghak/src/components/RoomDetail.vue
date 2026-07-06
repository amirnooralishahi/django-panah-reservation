<template>
  <Header />
  <div class="container py-5" dir="rtl">
    <div class="mb-3">
      <router-link to="/" class="btn btn-outline-secondary"
        >بازگشت به صفحه اصلی</router-link
      >
    </div>
    <div v-if="loading" class="text-center">
      در حال بارگذاری اطلاعات اقامتگاه…
    </div>
    <div v-else-if="errorMessage" class="alert alert-danger">
      {{ errorMessage }}
    </div>
    <div v-else class="detail-page">
      <div class="card shadow-sm border-0 overflow-hidden mb-4">
        <div class="row g-0">
          <div class="col-lg-7">
            <div class="p-4 p-lg-5">
              <div
                class="d-flex justify-content-between align-items-start gap-3 mb-3"
              >
                <div>
                  <h2 class="fw-bold mb-2">{{ roomTitle }}</h2>
                  <p class="text-muted mb-0">{{ roomLocation }}</p>
                </div>
                <span class="badge bg-success fs-6">{{ formattedPrice }}</span>
              </div>

              <p class="text-end text-secondary mb-4">{{ roomDescription }}</p>

              <div class="d-flex flex-wrap gap-2 mb-4">
                <span class="badge bg-light text-dark"
                  >ظرفیت: {{ roomCapacity }}</span
                >
                <span class="badge bg-light text-dark"
                  >تاریخ رزرو: {{ roomReserveDate }}</span
                >
                <span class="badge bg-light text-dark"
                  >میزبان: {{ roomOwner }}</span
                >
              </div>

              <div class="d-flex gap-3 flex-wrap">
                <span class="detail-pill"
                  ><i class="bi bi-house-door"></i> {{ roomBuildingInfo }}</span
                >
                <span class="detail-pill"
                  ><i class="bi bi-bed"></i> {{ roomBedService }}</span
                >
                <span class="detail-pill"
                  ><i class="bi bi-shower"></i> {{ roomToilet }}</span
                >
              </div>
            </div>
          </div>
          <div class="col-lg-5">
            <div class="gallery-wrapper">
              <img
                :src="galleryImages[0]"
                alt="تصویر اقامتگاه"
                class="gallery-main"
              />
              <div class="gallery-grid">
                <img
                  v-for="(image, index) in galleryImages.slice(1, 5)"
                  :key="index"
                  :src="image"
                  alt="تصویر اقامتگاه"
                />
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="row g-4">
        <div class="col-lg-8">
          <div class="card shadow-sm border-0 mb-4">
            <div class="card-body">
              <h5 class="fw-bold mb-3">درباره اقامتگاه</h5>
              <p class="text-end text-secondary mb-0">{{ roomDescription }}</p>
            </div>
          </div>

          <div class="card shadow-sm border-0 mb-4">
            <div class="card-body">
              <h5 class="fw-bold mb-3">امکانات و خدمات</h5>
              <div class="row g-3">
                <div
                  v-for="item in roomFacilities"
                  :key="item.label"
                  class="col-md-6"
                >
                  <div class="p-3 border rounded-3 h-100">
                    <div class="fw-bold mb-2">{{ item.label }}</div>
                    <div class="text-secondary">{{ item.value }}</div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="card shadow-sm border-0">
            <div class="card-body">
              <h5 class="fw-bold mb-3">جزئیات رزرو</h5>
              <div class="row g-3">
                <div class="col-md-6">
                  <div class="p-3 border rounded-3">
                    <div class="text-muted small">ظرفیت اقامت</div>
                    <div class="fw-bold">{{ roomCapacity }}</div>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="p-3 border rounded-3">
                    <div class="text-muted small">تاریخ در دسترس</div>
                    <div class="fw-bold">{{ roomReserveDate }}</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="col-lg-4">
          <div class="card shadow-sm border-0 sticky-card">
            <div class="card-body">
              <h5 class="fw-bold mb-3">رزرو و پرداخت</h5>
              <div class="border rounded p-3 mb-3">
                <div class="d-flex justify-content-between">
                  <span>قیمت هر شب</span>

                  <span>{{ formattedPrice }}</span>
                </div>

                <hr />

                <div class="d-flex justify-content-between">
                  <span>تعداد شب</span>

                  <span>{{ totalDays }}</span>
                </div>

                <hr />

                <div
                  class="d-flex justify-content-between fw-bold text-success"
                >
                  <span>مبلغ کل</span>

                  <span>{{ totalPrice.toLocaleString("fa-IR") }} تومان</span>
                </div>
              </div>
              <div class="mb-3">
                <label class="form-label">مبلغ پرداخت</label>
                <input
                  v-model="amount"
                  class="form-control"
                  type="number"
                  placeholder="مثلاً 500000"
                  readonly
                />

                <label class="form-label">تاریخ ورود</label>
                <input
                  v-model="reserveDate"
                  type="date"
                  class="form-control"
                  :min="today"
                />
                <div v-if="hasConflict" class="alert alert-danger mt-3">
                  این اقامتگاه در این بازه زمانی قبلاً رزرو شده است.
                </div>
                <label class="form-label">تاریخ خروج</label>
                <input
                  v-model="deliveryDate"
                  type="date"
                  class="form-control"
                  :min="reserveDate || today"
                />
              </div>
              <button
                class="btn btn-success w-100"
                @click="submitPayment"
                :disabled="hasConflict"
              >
                پرداخت
              </button>
              <div v-if="paymentMessage" class="alert alert-success mt-3 mb-0">
                {{ paymentMessage }}
              </div>
              <div v-if="paymentError" class="alert alert-danger mt-3 mb-0">
                {{ paymentError }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted, ref, watch } from "vue";
import { useRoute } from "vue-router";
import Header from "./header.vue";
import { fetchRoomById, payForRoom, fetchReservations } from "@/services/api";
const reservations = ref([]);
const route = useRoute();
const room = ref({});
const loading = ref(true);
const errorMessage = ref("");
const reserveDate = ref("");
const deliveryDate = ref("");
const amount = ref("");
const paymentMessage = ref("");
const paymentError = ref("");
const today = new Date().toISOString().split("T")[0];
const galleryImages = [
  "../../New_folder/room/1.webp",
  "../../New_folder/room/326a8c93-9f7a-4230-9384-2f04672d0dfe.webp",
  "../../New_folder/room/3d2e8edd-ea3f-43d1-a150-c527f0dd2a00.webp",
  "../../New_folder/room/51264bea-af1d-435f-9ec4-9c09f6c0627a.webp",
  "../../New_folder/room/653fe732-7139-4ac5-a519-0d9ad1c301b7.webp",
];

const roomTitle = computed(
  () => room.value?.Dormitory || room.value?.dormitory || "اقامتگاه",
);
const roomLocation = computed(
  () => room.value?.city || room.value?.location || "مکان ثبت نشده",
);
const roomDescription = computed(
  () =>
    room.value?.Additional_details ||
    room.value?.building_Information ||
    "توضیحات ثبت نشده",
);
const roomCapacity = computed(() => room.value?.Accommodation_cap || "نامشخص");
const roomBuildingInfo = computed(
  () => room.value?.building_Information || "ثبت نشده",
);
const roomBedService = computed(() => room.value?.Bed_Service || "ثبت نشده");
const roomToilet = computed(() => room.value?.Toilet_Bathroom || "ثبت نشده");
const roomReserveDate = computed(() => room.value?.time_reserve || "ثبت نشده");
const roomOwner = computed(() => room.value?.owner || "ثبت نشده");
const formattedPrice = computed(() => {
  const value = Number(room.value?.price ?? 0);
  return Number.isFinite(value)
    ? `${value.toLocaleString("fa-IR")} تومان`
    : "تماس بگیرید";
});
const roomFacilities = computed(() => [
  {
    label: "امکانات داخلی",
    value: room.value?.Internal_Faclities || "ثبت نشده",
  },
  { label: "نمای اقامتگاه", value: room.value?.Perspective || "ثبت نشده" },
  {
    label: "جزئیات تکمیلی",
    value: room.value?.Additional_details || "ثبت نشده",
  },
  {
    label: "اطلاعات بنا",
    value: room.value?.building_Information || "ثبت نشده",
  },
]);
const totalDays = computed(() => {
  if (!reserveDate.value || !deliveryDate.value) return 0;

  const start = new Date(reserveDate.value);
  const end = new Date(deliveryDate.value);

  const diff = end - start;

  if (diff <= 0) return 0;

  return Math.ceil(diff / (1000 * 60 * 60 * 24));
});
const totalPrice = computed(() => {
  const price = Number(room.value?.price || 0);

  return totalDays.value * price;
});
watch(totalPrice, (value) => {
  if (value > 0) {
    amount.value = value.toString();
  } else {
    amount.value = "";
  }
});
onMounted(async () => {
  try {
    room.value = await fetchRoomById(route.params.id);
    reservations.value = await fetchReservations(route.params.id);
  } catch (error) {
    errorMessage.value = error.message || "بارگذاری اقامتگاه با خطا مواجه شد.";
  } finally {
    loading.value = false;
  }
});

const submitPayment = async () => {
  paymentMessage.value = "";
  paymentError.value = "";
  if (hasConflict.value) {
    paymentError.value = "این بازه زمانی قبلاً رزرو شده است.";

    return;
  }
  console.log("reserveDate =", reserveDate.value)
console.log("deliveryDate =", deliveryDate.value)

console.log(
    new Date(deliveryDate.value),
    new Date(reserveDate.value)
)
  if (new Date(deliveryDate.value) <= new Date(reserveDate.value)) {
    paymentError.value = "تاریخ خروج باید بعد از تاریخ ورود باشد.";

    return;
  }
  if (totalDays.value === 0) {
    paymentError.value = "حداقل باید یک شب رزرو شود.";

    return;
  }
  if (!amount.value || !reserveDate.value || !deliveryDate.value) {
    paymentError.value = "لطفاً تاریخ ورود، تاریخ خروج و مبلغ را وارد کنید.";

    return;
  }

  try {
    const payload = {
      room_id: room.value.id,
      amount: amount.value,
      passenger_slug: localStorage.getItem("profile_slug") || "",

      reserve_date: reserveDate.value,
      delivery_date: deliveryDate.value,
    };
    const result = await payForRoom(payload);
    paymentMessage.value = result.message || "پرداخت با موفقیت ثبت شد.";
  } catch (error) {
    paymentError.value = error.message || "پرداخت انجام نشد.";
  }
};
const hasConflict = computed(() => {
  if (!reserveDate.value || !deliveryDate.value) return false;

  const start = new Date(reserveDate.value);
  const end = new Date(deliveryDate.value);

  return reservations.value.some((item) => {
    const reserveStart = new Date(item.start);
    const reserveEnd = new Date(item.end);

    return start < reserveEnd && end > reserveStart;
  });
});
</script>

<style scoped>
.detail-page {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.gallery-wrapper {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  padding: 1rem;
  background: #f7f9fc;
  height: 100%;
}

.gallery-main {
  width: 100%;
  height: 280px;
  object-fit: cover;
  border-radius: 16px;
}

.gallery-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 0.75rem;
}

.gallery-grid img {
  width: 100%;
  height: 110px;
  object-fit: cover;
  border-radius: 12px;
}

.detail-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  padding: 0.7rem 0.9rem;
  border-radius: 999px;
  background: #f4f7fb;
  color: #405064;
}

.sticky-card {
  position: sticky;
  top: 1rem;
}
</style>
