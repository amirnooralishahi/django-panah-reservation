<template>
  <div class="register-page d-flex flex-column align-items-center justify-content-center py-5">
    <div class="register-card rounded-4 shadow-sm p-4 w-100">
      <div class="header-section text-center mb-4">
        <h1>ثبت‌نام در پناه</h1>
        <p>برای رزرو اقامتگاه، حساب کاربری جدید بسازید.</p>
      </div>

      <div class="form-section d-flex flex-column gap-3">
        <input v-model="form.username" placeholder="نام کاربری" />
        <input v-model="form.email" type="email" placeholder="ایمیل" />
        <input v-model="form.password" type="password" placeholder="رمز عبور" />
        <input v-model="form.national_code" placeholder="کد ملی" />

        <button class="submit-button" @click="submitRegister">ثبت‌نام</button>

        <div v-if="successMessage" class="alert alert-success">{{ successMessage }}</div>
        <div v-if="errorMessage" class="alert alert-danger">{{ errorMessage }}</div>

        <div class="text-center">
          <router-link to="/login">قبلاً حساب دارید؟ ورود</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import { register } from '@/services/api'

const router = useRouter()
const form = reactive({
  username: '',
  email: '',
  password: '',
  national_code: '',
})
const errorMessage = ref('')
const successMessage = ref('')

const submitRegister = async () => {
  errorMessage.value = ''
  successMessage.value = ''

  try {
    await register(form)
    successMessage.value = 'ثبت‌نام با موفقیت انجام شد.'
    router.push('/')
  } catch (error) {
    errorMessage.value = error.message || 'ثبت‌نام با خطا مواجه شد.'
  }
}
</script>

<style scoped>
.register-page {
  min-height: 100vh;
  background: linear-gradient(180deg, #f7f9fc 0%, #e8edf4 100%);
  padding: 40px 12px;
}
.register-card {
  max-width: 560px;
  width: 100%;
  background: #fff;
  border: 1px solid rgba(72, 72, 78, 0.08);
}
input {
  width: 100%;
  padding: 12px 14px;
  border-radius: 12px;
  border: 1px solid rgba(72, 72, 78, 0.15);
}
.submit-button {
  width: 100%;
  padding: 12px 14px;
  border: none;
  border-radius: 12px;
  background: #3a8a54;
  color: white;
  font-weight: 700;
}
</style>
