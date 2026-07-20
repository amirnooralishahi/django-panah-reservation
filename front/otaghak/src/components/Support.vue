<template>
  <div class="support-page d-flex flex-column align-items-center py-5">
    <div class="support-card rounded-4 shadow-sm p-4 w-100">
      <div class="header-section text-center mb-3">
        <h2>پشتیبانی پناه</h2>
        <p class="mb-0">ما اینجا هستیم تا به شما کمک کنیم. در شرایط اضطراری یا برای مسائل فنی، با ما تماس بگیرید.</p>
      </div>

      <div class="contact row mt-4">
        <div class="col-12 mb-3">
          <strong>آیدی پشتیبانی در ایتا:</strong>
          <a href="id: @ava_shn">ava_shn</a>
        </div>
        <div class="col-12 mb-3">
          <strong>ایمیل پشتیبانی:</strong>
          <a href="mailto:avashahabi@gmail.com">avashahabi@gmail.com</a>
        </div>
        <div class="col-12 mb-3">
          <strong>ساعات پاسخگویی:</strong>
          <div>روزهای هفته ۹:۰۰ تا ۱۸:۰۰</div>
        </div>
      </div>

      <div class="help-resources mt-3">
        <h4>منابع و راهنمایی</h4>
        <ul>
          <li>راهنمای ثبت و مدیریت اقامتگاه</li>
          <li>سوالات متداول درباره رزرو و لغو</li>
          <li>راهنمای ایمنی و قوانین در شرایط اضطراری</li>
        </ul>
      </div>

      <div class="emergency-note mt-4 text-muted">
        اگر در وضعیت جنگی یا سایر شرایط اضطراری هستید و نیاز به کمک فوری دارید، لطفاً ابتدا با شماره‌های رسمی امدادی کشور تماس بگیرید و سپس در صورت نیاز با پشتیبانی ما ارتباط برقرار کنید.
      </div>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.support-page { min-height: 60vh; padding: 36px 12px; }
.support-card { max-width: 760px; background: #fff; border: 1px solid rgba(72,72,78,0.06); }
.support-card a { color: #0b5ed7; text-decoration: none; font-weight: 600; }
.help-resources ul { margin: 8px 0 0 16px; }
</style>
