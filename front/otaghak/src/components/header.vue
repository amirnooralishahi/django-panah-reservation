<template>
  <header class="w-100 d-flex flex-column position-sticky">
    <div class="down">
      <div class="header d-flex justify-content-center">
        <div class="header-contain d-flex">
          <div class="right w-50 d-flex align-items-center jgap-3">
            <div class="p-2 header-action header-login">
              <template v-if="isLoggedIn">
                <div class="d-flex align-items-center gap-2">
                  <router-link
                    to="/profile"
                    class="btn btn-sm btn-outline-primary rounded-pill"
                  >
                    پروفایل
                  </router-link>
                  <button
                    type="button"
                    class="btn btn-sm btn-outline-danger rounded-pill"
                    @click="logout"
                  >
                    خروج
                  </button>
                  <span class="fw-bold text-success"
                    >سلام، {{ displayName }}</span
                  >
                </div>
              </template>
              <template v-else>
                <router-link
                  to="/login"
                  class="d-flex align-items-center gap-1 header-link"
                >
                  <span class="text">ورود/ثبت نام</span>
                  <svg
                    width="24"
                    height="24"
                    fill="none"
                    viewBox="0 0 24 24"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      d="M12 15C15.3137 15 18 12.3137 18 9C18 5.68629 15.3137 3 12 3C8.68629 3 6 5.68629 6 9C6 12.3137 8.68629 15 12 15Z"
                      stroke="#48484E"
                      strokeWidth="2"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                    />
                    <path
                      d="M2.90625 20.25C3.82775 18.6536 5.15328 17.3278 6.74958 16.4061C8.34588 15.4844 10.1567 14.9991 12 14.9991C13.8433 14.9991 15.6541 15.4844 17.2504 16.4061C18.8467 17.3278 20.1722 18.6536 21.0938 20.25"
                      stroke="#48484E"
                      strokeWidth="2"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                    />
                  </svg>
                </router-link>
              </template>
            </div>
            <div class="p-2 header-action header-support">
              <router-link
                to="/support"
                class="d-flex align-items-center gap-1 header-link"
              >
                <span class="text">پشتیبانی</span>
                <svg
                  height="24"
                  width="24"
                  fill="none"
                  viewBox="0 0 24 24"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <g clip-path="url(#clip0_1257_30563)">
                    <path
                      d="M12.0004 1.9C6.98039 1.9 2.90039 5.97 2.90039 10.98V16.09C2.90039 17.71 4.22039 19.04 5.85039 19.04C7.48039 19.04 8.80039 17.72 8.80039 16.09V14.05C8.80039 12.43 7.48039 11.1 5.85039 11.1C5.44039 11.1 5.05039 11.18 4.70039 11.33V10.97C4.70039 6.96 7.97039 3.69 12.0004 3.69C16.0304 3.69 19.3004 6.95 19.3004 10.97V11.33C18.9504 11.18 18.5604 11.1 18.1504 11.1C16.5204 11.1 15.2004 12.42 15.2004 14.05V16.09C15.2004 17.28 15.9204 18.31 16.9404 18.77C16.2604 19.53 14.4904 20.3 12.0004 20.3C11.5004 20.3 11.1004 20.7 11.1004 21.2C11.1004 21.7 11.5004 22.1 12.0004 22.1C15.5404 22.1 18.3104 20.78 18.9204 18.92C20.1704 18.58 21.1004 17.45 21.1004 16.09V10.98C21.1004 5.97 17.0204 1.9 12.0004 1.9ZM5.85039 12.9C6.48039 12.9 7.00039 13.41 7.00039 14.04V16.08C7.00039 16.71 6.48039 17.22 5.85039 17.22C5.22039 17.22 4.70039 16.71 4.70039 16.08V14.04C4.70039 13.41 5.22039 12.9 5.85039 12.9ZM19.3004 16.09C19.3004 16.72 18.7804 17.23 18.1504 17.23C17.5204 17.23 17.0004 16.72 17.0004 16.09V14.05C17.0004 13.42 17.5204 12.91 18.1504 12.91C18.7804 12.91 19.3004 13.42 19.3004 14.05V16.09Z"
                      stroke="#48484E"
                      stroke-width="2"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                    />
                  </g>
                </svg>
              </router-link>
            </div>

            <div class="p-2 header-action header-host">
              <router-link
                to="/host"
                class="d-flex align-items-center gap-1 header-link"
              >
                <span class="text">میزبان شوید</span>
                <i class="bi bi-house-add-fill"></i>
              </router-link>
            </div>
          </div>
          <div
            class="left w-50 d-flex justify-content-end align-items-center gap-1"
          >
            <div class="d-flex align-items-center gap-3">
              <router-link to="/" class="btn btn-outline-secondary"
                >بازگشت به صفحه اصلی</router-link
              >
              <span>سامانه ی پناه</span>
              <img src="../../New_folder/logo.jpg" alt="" class="logo" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const isLoggedIn = ref(false);
const displayName = ref("");

function syncAuthState() {
  const token = localStorage.getItem("access_token");
  const storedName = localStorage.getItem("user_name");
  isLoggedIn.value = Boolean(token);
  displayName.value = storedName || "کاربر";
}

function logout() {
  localStorage.removeItem("access_token");
  localStorage.removeItem("profile_slug");
  localStorage.removeItem("user_name");
  syncAuthState();
  router.push("/");
}

onMounted(() => {
  syncAuthState();
  window.addEventListener("auth:changed", syncAuthState);
});

onBeforeUnmount(() => {
  window.removeEventListener("auth:changed", syncAuthState);
});
</script>

<style>
@import "../assets/header.css";
</style>
