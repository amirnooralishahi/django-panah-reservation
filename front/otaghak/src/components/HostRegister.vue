<template>
  <Header />
  <div class="host-page d-flex flex-column align-items-center py-5">
    <div class="host-card rounded-4 shadow-sm p-4 w-100">
      <div class="header-section text-center mb-3">
        <h2>میزبان شوید — فرم ثبت‌نام میزبان</h2>
        <p class="mb-0">
          اگر می‌خواهید فضای خود را میزبان کنید، لطفاً فرم زیر را تکمیل کنید تا
          تیم ما با شما تماس بگیرد.
        </p>
      </div>

      <div class="form-section d-flex flex-column gap-3 mt-3">
        <div class="form-row">
          <label class="form-label">نام شهر</label>
          <input v-model="form.city" placeholder="شهر" />
        </div>

        <div class="form-row">
          <label class="form-label">محل اقامت</label>
          <input v-model="form.location" placeholder="محل اقامت" />
        </div>

        <div class="form-row">
          <label class="form-label">عنوان اقامتگاه (اختیاری)</label>
          <input
            v-model="form.Dormitory"
            type="text"
            placeholder="مثلاً ویلا در شمال"
          />
        </div>

        <div class="form-row">
          <label class="form-label">توضیح کوتاه درباره اقامتگاه</label>
          <textarea v-model="form.building_Information"></textarea>
        </div>
        <div class="form-row">
          <label class="form-label"> سرویس بهداشتی </label>
          <input v-model="form.Toilet_Bathroom" />
        </div>
        <div class="form-row">
          <label class="form-label">سرویس خواب </label>
          <input v-model="form.Bed_Service" />
        </div>
        <div class="form-row">
          <label class="form-label"> ظرفیت </label>
          <input v-model="form.Accommodation_cap" />
        </div>
        <div class="form-row">
          <label class="form-label"> چشم انداز </label>
          <textarea v-model="form.Perspective"></textarea>
        </div>
        <div class="form-row">
          <label class="form-label">امکانات </label>
          <textarea v-model="form.Internal_Faclities"></textarea>
        </div>
        <div class="form-row">
          <label class="form-label">توضیحات </label>
          <textarea v-model="form.Additional_details"></textarea>
        </div>
        <div class="form-row">
          <label class="form-label"> تاریخ</label>
          <input type="date" v-model="form.time_reserve" />
        </div>
        <div class="form-row">
          <label class="form-label">قیمت </label>
          <input type="number" v-model="form.price" />
        </div>

        <div class="form-row">
          <label class="form-label">بارگذاری تصویر (اختیاری)</label>
          <input
            type="file"
            multiple
            accept="image/*"
            @change="onFileSelected"
          />
          <div v-if="pictureName" class="text-muted small mt-1">
            فایل انتخاب شده: {{ pictureName }}
          </div>
        </div>

        <div class="d-flex gap-2 flex-wrap align-items-center">
          <button class="btn-submit" @click="submitRoom">ثبت اقامتگاه</button>
        </div>

        <div v-if="successMessage" class="alert alert-success mt-3">
          {{ successMessage }}
        </div>
        <div v-if="errorMessage" class="alert alert-danger mt-3">
          {{ errorMessage }}
        </div>

        <div class="note text-muted mt-2">
          تیم پناه پس از بررسی درخواست با شما تماس خواهد گرفت. اطلاعات شما
          محرمانه نگه داشته می‌شود.
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
// import {reactive, ref } from "vue";
// import { useRouter } from "vue-router";
// import { createRoomWithImages } from "@/services/api.js";
// import Header from "./header.vue";
// const router = useRouter();

// const name = ref("");
// const contact = ref("");
// const propertyTitle = ref("");
// const description = ref("");
// const picture = ref(null);
// const pictureName = ref("");
// const errorMessage = ref("");
// const successMessage = ref("");

// const resetForm = () => {
//   name.value = "";
//   contact.value = "";
// propertyTitle.value = "";
//   description.value = "";
//   picture.value = null;
//   pictureName.value = "";
//   errorMessage.value = "";
//   successMessage.value = "";
// };

// const onFileSelected = (event) => {
//   const file = event.target.files?.[0];
//   if (file) {
//     picture.value = file;
//     pictureName.value = file.name;
//   } else {
//     picture.value = null;
//     pictureName.value = "";
//   }
// };

// const submitHost = async () => {
//   errorMessage.value = "";
//   successMessage.value = "";

//   if (!name.value || !contact.value) {
//     errorMessage.value = "لطفاً نام و شماره تماس/ایمیل را وارد کنید.";
//     return;
//   }

//   try {
//     const payload = new FormData();
//     payload.append("name", name.value);
//     payload.append("contact", contact.value);
//     payload.append("propertyTitle", propertyTitle.value);
//     payload.append("description", description.value);
//     if (picture.value) {
//       payload.append("picture", picture.value);
//     }

//     successMessage.value = "درخواست میزبان با موفقیت به سرور ارسال شد.";
//     resetForm();
//   } catch (error) {
//     errorMessage.value =
//       error.message || "خطا در ارسال درخواست. دوباره تلاش کنید.";
//   }
// };
import { reactive, ref } from "vue";
import { useRouter } from "vue-router";
import { createRoomWithImages } from "@/services/api";
import Header from "./header.vue";

const router = useRouter();

const form = reactive({
  location: "",
  city: "",
  Dormitory: "",
  building_Information: "",
  Bed_Service: "",
  Toilet_Bathroom: "",
  Accommodation_cap: "",
  Perspective: "",
  Internal_Faclities: "",
  Additional_details: "",
  time_reserve: "",
  price: "",
});

const images = ref([]);
const pictureName = ref("");

const onFileSelected = (event) => {
  images.value = Array.from(event.target.files);

  pictureName.value = images.value.map((img) => img.name).join(" , ");
};
const successMessage = ref("");
const errorMessage = ref("");
const submitRoom = async () => {
  successMessage.value = "";
  errorMessage.value = "";

  try {
    const payload = {
      ...form,
      images: images.value,
    };

    await createRoomWithImages(payload);

    successMessage.value = "اقامتگاه با موفقیت ثبت شد.";

    router.push("/");
  } catch (err) {
    errorMessage.value = err.message || "خطا در ثبت اقامتگاه";
  }
};
</script>

<style scoped>
.host-page {
  min-height: 60vh;
  padding: 36px 12px;
}
.host-card {
  max-width: 760px;
  background: #fff;
  border: 1px solid rgba(72, 72, 78, 0.06);
}
.header-section h2 {
  margin-bottom: 6px;
  font-size: 1.5rem;
}
.form-row {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.form-row input,
.form-row textarea {
  padding: 12px 14px;
  border: 1px solid rgba(72, 72, 78, 0.12);
  border-radius: 10px;
}
.btn-submit {
  background: #3a8a54;
  color: white;
  padding: 10px 14px;
  border-radius: 10px;
  border: none;
  cursor: pointer;
}
.btn-cancel {
  background: transparent;
  border: 1px solid rgba(72, 72, 78, 0.12);
  padding: 10px 14px;
  border-radius: 10px;
  cursor: pointer;
}
.note {
  font-size: 0.95rem;
}
</style>
