<template>
  <router-link :to="`/room/${room?.id ?? ''}`" class="text-decoration-none text-dark">
    <div class="room-card rounded-4 overflow-hidden border shadow-sm h-100">
      <div class="room-image-wrapper position-relative">
        <img :src="image" :alt="roomTitle" class="room-image" />
        <span class="room-badge">اقامتگاه</span>
      </div>
      <div class="p-3">
        <div class="d-flex justify-content-between align-items-start gap-2 mb-2">
          <span class="fw-bold text-success">{{ formattedPrice }}</span>
          <h5 class="mb-0 text-end fw-bold">{{ roomTitle }}</h5>
        </div>
        <p class="text-muted text-end mb-2">{{ roomLocation }}</p>
        <p class="text-end mb-3 small text-secondary">{{ roomDescription }}</p>
        <div class="d-flex justify-content-between align-items-center">
          <span class="badge bg-light text-dark">{{ roomCapacity }}</span>
          <span class="text-muted small">ظرفیت</span>
        </div>
      </div>
    </div>
  </router-link>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  room: {
    type: Object,
    default: () => ({})
  },
  image: {
    type: String,
    default: ''
  }
})

const roomTitle = computed(() => props.room?.Dormitory || props.room?.dormitory || 'اقامتگاه')
const roomLocation = computed(() => props.room?.city || props.room?.location || 'مکان ثبت نشده')
const roomDescription = computed(() => props.room?.Additional_details || props.room?.building_Information || 'توضیحات ثبت نشده')
const roomCapacity = computed(() => props.room?.Accommodation_cap || 'نامشخص')
const formattedPrice = computed(() => {
  const value = Number(props.room?.price ?? 0)
  return Number.isFinite(value) ? `${value.toLocaleString('fa-IR')} تومان` : 'تماس بگیرید'
})
</script>

<style scoped>
.room-card {
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  background: #fff;
}

.room-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 0.75rem 1.5rem rgba(0, 0, 0, 0.12) !important;
}

.room-image-wrapper {
  height: 220px;
  background: #f4f7fb;
}

.room-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.room-badge {
  position: absolute;
  top: 12px;
  left: 12px;
  background: rgba(0, 0, 0, 0.62);
  color: white;
  padding: 6px 10px;
  border-radius: 999px;
  font-size: 0.8rem;
}
</style>