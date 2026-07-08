<template>
  <Header />
  <div class="container py-5" dir="rtl">
    <div class="mb-3">
      <router-link to="/" class="btn btn-outline-secondary">بازگشت به صفحه اصلی</router-link>
    </div>
    <div class="card shadow-sm border-0">
      <div class="card-body">
        <div class="d-flex flex-column flex-md-row justify-content-between align-items-start gap-3 mb-4">
          <div>
            <h2 class="fw-bold mb-2">{{ isHost ? 'پروفایل میزبان' : 'پروفایل کاربر' }}</h2>
            <p class="text-muted mb-0">{{ isHost ? 'اطلاعات میزبان و مدیریت اقامتگاه‌ها' : 'اطلاعات شخصی و رزروهای شما' }}</p>
          </div>
          <span class="badge rounded-pill" :class="isHost ? 'bg-success' : 'bg-primary'">{{ isHost ? 'میزبان' : 'کاربر عادی' }}</span>
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
                      <input v-model="profile.username" class="form-control" type="text" disabled />
                    </div>
                    <div class="col-md-6">
                      <label class="form-label">کد ملی</label>
                      <input v-model="profile.NationalCode" class="form-control" type="text" disabled />
                    </div>
                    <div class="col-md-6">
                      <label class="form-label">ایمیل</label>
                      <input v-model="profile.email" class="form-control" type="email" />
                    </div>
                    <div class="col-md-6">
                      <label class="form-label">شماره همراه</label>
                      <input v-model="profile.phone" class="form-control" type="text" />
                    </div>
                    <div class="col-md-6">
                      <label class="form-label">شغل</label>
                      <input v-model="profile.Job_title" class="form-control" type="text" />
                    </div>
                    <div class="col-md-6">
                      <label class="form-label">شناسه پروفایل</label>
                      <input v-model="profile.slug" class="form-control" type="text" disabled />
                    </div>
                  </div>

                  <button class="btn btn-success mt-4" @click="saveProfile">ذخیره تغییرات</button>
                  <div v-if="message" class="alert alert-success mt-3 mb-0">{{ message }}</div>
                </div>
              </div>
            </div>
          </div>

          <div class="col-lg-4">
            <div class="card border-0 bg-dark text-white">
              <div class="card-body">
                <h5 class="fw-bold mb-3">نمای کلی</h5>
                <ul class="list-unstyled mb-0">
                  <li class="mb-2">نام کاربری: {{ profile.username || '---' }}</li>
                  <li class="mb-2">ایمیل: {{ profile.email || '---' }}</li>
                  <li>شغل: {{ profile.Job_title || '---' }}</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'
import Header from './header.vue'
import { fetchRooms, fetchUserProfile, updateRoom, updateUserProfile } from '@/services/api'

const isHost = computed(() => (typeof window !== 'undefined' ? localStorage.getItem('user_role') : 'guest') === 'host')
const message = ref('')
const error = ref('')
const hostRoomError = ref('')
const profile = ref({
  username: '',
  slug: '',
  email: '',
  phone: '',
  NationalCode: '',
  Job_title: '',
  id: null,
})
const hostRooms = ref([])
const editingRoomId = ref(null)
const roomEdits = ref({})

function getMediaUrl(path) {
  if (!path) return ''
  if (path.startsWith('http') || path.startsWith('/')) {
    return path
  }
  return `/${path}`
}

async function loadHostRooms(ownerId) {
  if (!ownerId) {
    hostRooms.value = []
    return
  }

  try {
    hostRoomError.value = ''
    const data = await fetchRooms()
    const rooms = Array.isArray(data) ? data : data?.results || []
    hostRooms.value = rooms.filter(room => String(room.owner) === String(ownerId))
  } catch (err) {
    hostRoomError.value = err.message || 'بارگذاری اقامتگاه‌های میزبان با خطا مواجه شد.'
    hostRooms.value = []
  }
}

async function loadProfile() {
  message.value = ''
  error.value = ''

  if (!localStorage.getItem('access_token')) {
    error.value = 'برای دسترسی به پروفایل ابتدا وارد شوید.'
    return
  }

  try {
    const data = await fetchUserProfile()
    profile.value = {
      username: localStorage.getItem('user_name') || '',
      slug: data.slug || '',
      email: data.email || '',
      phone: data.phone || '',
      NationalCode: data.NationalCode || '',
      Job_title: data.Job_title || '',
      id: data.id || null,
    }

    if (profile.value.id) {
      localStorage.setItem('profile_id', profile.value.id)
    }

    if (isHost.value) {
      const ownerId = profile.value.id || localStorage.getItem('profile_id')
      await loadHostRooms(ownerId)
    }
  } catch (err) {
    error.value = err.message || 'بارگذاری اطلاعات پروفایل با خطا مواجه شد.'
  }
}

async function saveProfile() {
  message.value = ''
  error.value = ''
  try {
    const updateData = {
      email: profile.value.email,
      phone: profile.value.phone,
      Job_title: profile.value.Job_title,
    }
    const result = await updateUserProfile(updateData)
    profile.value = {
      ...profile.value,
      email: result.email || profile.value.email,
      phone: result.phone || profile.value.phone,
      Job_title: result.Job_title || profile.value.Job_title,
    }
    message.value = 'تغییرات با موفقیت ذخیره شد.'
  } catch (err) {
    error.value = err.message || 'ذخیره‌سازی با خطا مواجه شد.'
  }
}

function startEditRoom(room) {
  editingRoomId.value = room.id
  roomEdits.value = {
    location: room.location || '',
    city: room.city || '',
    price: room.price || '',
    Dormitory: room.Dormitory || '',
    building_Information: room.building_Information || '',
    Bed_Service: room.Bed_Service || '',
    Toilet_Bathroom: room.Toilet_Bathroom || '',
    Internal_Faclities: room.Internal_Faclities || '',
    Additional_details: room.Additional_details || '',
  }
}

function cancelEditRoom() {
  editingRoomId.value = null
  roomEdits.value = {}
}

async function saveRoom(roomId) {
  try {
    const updated = await updateRoom(roomId, roomEdits.value)
    const index = hostRooms.value.findIndex(room => room.id === roomId)
    if (index !== -1) {
      hostRooms.value[index] = { ...hostRooms.value[index], ...updated }
    }
    editingRoomId.value = null
    message.value = 'اطلاعات اقامتگاه با موفقیت به‌روزرسانی شد.'
  } catch (err) {
    error.value = err.message || 'خطا در به‌روزرسانی اقامتگاه.'
  }
}

onMounted(loadProfile)
</script>

<style scoped>
.card {
  border-radius: 1rem;
}
</style>