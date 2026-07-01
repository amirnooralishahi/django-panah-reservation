<template>
  <div class="host-page d-flex flex-column align-items-center py-5">
    <div class="host-card rounded-4 shadow-sm p-4 w-100">
      <div class="header-section text-center mb-3">
        <h2>میزبان شوید — فرم ثبت‌نام میزبان</h2>
        <p class="mb-0">اگر می‌خواهید فضای خود را میزبان کنید، لطفاً فرم زیر را تکمیل کنید تا تیم ما با شما تماس بگیرد.</p>
      </div>

      <div class="form-section d-flex flex-column gap-3 mt-3">
        <div class="form-row">
          <label class="form-label">نام و نام خانوادگی</label>
          <input v-model="name" type="text" placeholder="مثلاً علی رضایی" />
        </div>

        <div class="form-row">
          <label class="form-label">ایمیل یا شماره همراه</label>
          <input v-model="contact" type="text" placeholder="مثلاً example@mail.com یا 0912xxxxxxx" />
        </div>

        <div class="form-row">
          <label class="form-label">عنوان اقامتگاه (اختیاری)</label>
          <input v-model="propertyTitle" type="text" placeholder="مثلاً ویلا در شمال" />
        </div>

        <div class="form-row">
          <label class="form-label">توضیح کوتاه درباره اقامتگاه</label>
          <textarea v-model="description" rows="3" placeholder="حداکثر 300 کاراکتر"></textarea>
        </div>

        <div class="d-flex gap-2">
          <button class="btn-submit" @click="submitHost">ارسال درخواست</button>
          <button class="btn-cancel" @click="resetForm">پاک کردن</button>
        </div>

        <div v-if="successMessage" class="alert alert-success mt-3">
          {{ successMessage }}
        </div>
        <div v-if="errorMessage" class="alert alert-danger mt-3">
          {{ errorMessage }}
        </div>

        <div class="note text-muted mt-2">
          تیم پناه پس از بررسی درخواست با شما تماس خواهد گرفت. اطلاعات شما محرمانه نگه داشته می‌شود.
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { sendHostRequest } from '@/services/api'

const name = ref('')
const contact = ref('')
const propertyTitle = ref('')
const description = ref('')
const errorMessage = ref('')
const successMessage = ref('')

const resetForm = () => {
  name.value = ''
  contact.value = ''
  propertyTitle.value = ''
  description.value = ''
  errorMessage.value = ''
  successMessage.value = ''
}

const submitHost = async () => {
  errorMessage.value = ''
  successMessage.value = ''

  if (!name.value || !contact.value) {
    errorMessage.value = 'لطفاً نام و شماره تماس/ایمیل را وارد کنید.'
    return
  }

  try {
    await sendHostRequest({
      name: name.value,
      contact: contact.value,
      propertyTitle: propertyTitle.value,
      description: description.value,
    })
    successMessage.value = 'درخواست میزبان با موفقیت به سرور ارسال شد.'
    resetForm()
  } catch (error) {
    errorMessage.value = error.message || 'خطا در ارسال درخواست. دوباره تلاش کنید.'
  }
}
</script>

<style scoped>
.host-page { min-height: 60vh; padding: 36px 12px; }
.host-card { max-width: 760px; background: #fff; border: 1px solid rgba(72,72,78,0.06); }
.header-section h2 { margin-bottom: 6px; font-size: 1.5rem; }
.form-row { display: flex; flex-direction: column; gap: 8px; }
.form-row input, .form-row textarea { padding: 12px 14px; border: 1px solid rgba(72,72,78,0.12); border-radius: 10px; }
.btn-submit { background: #3a8a54; color: white; padding: 10px 14px; border-radius: 10px; border: none; cursor: pointer; }
.btn-cancel { background: transparent; border: 1px solid rgba(72,72,78,0.12); padding: 10px 14px; border-radius: 10px; cursor: pointer; }
.note { font-size: 0.95rem; }
</style>
