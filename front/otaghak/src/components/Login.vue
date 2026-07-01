<template>
  <div class="login-page d-flex flex-column align-items-center justify-content-center py-5">
    <div class="login-card rounded-4 shadow-sm p-4 w-100">
      <div class="header-section d-flex flex-column align-items-center text-center mb-4">
        <h1>ورود به سامانه پناه</h1>
        <p class="mb-0">برای متقاضیان خانه و میزبانان گرامی، وارد شوید تا دسترسی سریع به خدمات فراهم شود.</p>
      </div>

      <div class="role-select d-flex flex-column flex-md-row gap-3 mb-4">
        <button
          :class="['role-button', selectedRole === 'guest' ? 'active' : '']"
          @click="selectRole('guest')"
        >
          متقاضی خانه
        </button>
        <button
          :class="['role-button', selectedRole === 'host' ? 'active' : '']"
          @click="selectRole('host')"
        >
          میزبان خانه‌دار
        </button>
      </div>

      <div class="info-box mb-4">
        <p class="mb-1"><strong>نکته:</strong> لطفاً نقش خود را انتخاب کنید تا فرم مناسب نمایش داده شود.</p>
        <p class="mb-0">اگر هنوز عضو نشده‌اید، پس از انتخاب نقش می‌توانید از طریق گزینه ثبت نام وارد شوید.</p>
      </div>

      <div class="form-section d-flex flex-column gap-3">
        <div class="form-row d-flex flex-column gap-3">
          <label class="form-label">ایمیل یا شماره همراه</label>
          <input type="text" placeholder="مثلاً example@mail.com یا 0912xxxxxxx" v-model="username" />
        </div>

        <div class="form-row d-flex flex-column gap-3">
          <label class="form-label">رمز عبور</label>
          <input type="password" placeholder="رمز عبور خود را وارد کنید" v-model="password" />
        </div>

        <div class="additional-info text-end">
          <span class="role-text">نقش انتخاب‌شده: {{ selectedRole === 'guest' ? 'متقاضی خانه' : 'میزبان خانه‌دار' }}</span>
        </div>

        <button class="submit-button" @click="submitLogin">
          ورود به عنوان {{ selectedRole === 'guest' ? 'متقاضی' : 'میزبان' }}
        </button>

        <div v-if="successMessage" class="alert alert-success mt-3">
          {{ successMessage }}
        </div>
        <div v-if="errorMessage" class="alert alert-danger mt-3">
          {{ errorMessage }}
        </div>

        <div class="register-note text-center text-muted">
          هنوز حساب کاربری ندارید؟ <router-link to="/register">ثبت نام کنید</router-link> و به جمع همراهان پناه بپیوندید.
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { login } from '@/services/api'

const router = useRouter()
const route = useRoute()
const selectedRole = ref('guest')
const username = ref('')
const password = ref('')
const errorMessage = ref('')
const successMessage = ref('')

onMounted(() => {
  if (route.query.role === 'host') {
    selectedRole.value = 'host'
  }
})

const selectRole = (role) => {
  selectedRole.value = role
}

const submitLogin = async () => {
  errorMessage.value = ''
  successMessage.value = ''

  if (!username.value || !password.value) {
    errorMessage.value = 'لطفاً نام کاربری و رمز عبور را وارد کنید.'
    return
  }

  try {
    await login(username.value, password.value)
    localStorage.setItem('user_role', selectedRole.value === 'host' ? 'host' : 'guest')
    window.dispatchEvent(new Event('auth:changed'))
    successMessage.value = 'ورود با موفقیت انجام شد. اکنون می‌توانید به بخش‌های دیگر بروید.'
    router.push(selectedRole.value === 'host' ? '/host' : '/')
  } catch (error) {
    errorMessage.value = error.message || 'خطا در ورود. مجدداً تلاش کنید.'
  }
}
</script>

<style scoped>
.login-page {
  min-height: 100vh;
  padding: 40px 12px;
  background: linear-gradient(180deg, #f7f9fc 0%, #e8edf4 100%);
}

.login-card {
  max-width: 640px;
  background: #ffffff;
  border: 1px solid rgba(72, 72, 78, 0.08);
}

.header-section h1 {
  font-size: 2rem;
  margin-bottom: 0.75rem;
  color: #1d242f;
}

.header-section p {
  font-size: 1rem;
  color: #5f6670;
}

.role-select {
  justify-content: center;
}

.role-button {
  flex: 1;
  min-width: 160px;
  padding: 14px 18px;
  border: 1px solid rgba(72, 72, 78, 0.15);
  border-radius: 14px;
  background: #f7f8fb;
  color: #48484e;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.25s ease;
}

.role-button.active,
.role-button:hover {
  background: #3a8a54;
  color: #ffffff;
  border-color: #3a8a54;
}

.info-box {
  background: #f4f7fb;
  padding: 18px 20px;
  border-radius: 16px;
  color: #4f5560;
  font-size: 0.95rem;
}

.form-row input {
  width: 100%;
  padding: 14px 16px;
  border: 1px solid rgba(72, 72, 78, 0.15);
  border-radius: 12px;
  font-size: 1rem;
  color: #2a2f36;
  background: #ffffff;
}

.form-row input::placeholder {
  color: rgba(72, 72, 78, 0.45);
}

.form-label {
  font-size: 0.95rem;
  color: #48484e;
}

.additional-info {
  font-size: 0.95rem;
  color: #5f6670;
}

.role-text {
  display: inline-block;
  padding: 6px 12px;
  border-radius: 999px;
  background: rgba(58, 138, 84, 0.1);
  color: #2f5238;
}

.submit-button {
  width: 100%;
  padding: 14px 16px;
  border: none;
  border-radius: 14px;
  background: #3a8a54;
  color: white;
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  transition: background 0.25s ease;
}

.submit-button:hover {
  background: #2f6c41;
}

.register-note {
  color: #6b7280;
  font-size: 0.95rem;
}

.register-note a {
  color: #3a8a54;
  text-decoration: none;
  font-weight: 600;
}
</style>
