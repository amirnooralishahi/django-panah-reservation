<template>
  <div class="support-page d-flex flex-column align-items-center py-5">

    <div class="support-card rounded-4 shadow-sm p-4 w-100">

      <div class="header-section text-center mb-4">
        <h2>قوانین و مقررات رزرو</h2>
        <p class="mb-0">
          لطفاً پیش از ثبت رزرو، قوانین زیر را مطالعه کنید.
        </p>
      </div>

      <div class="mt-3">
        <ol class="rules-list">
          <li>تمام اطلاعات واردشده توسط کاربر باید صحیح و واقعی باشد.</li>

          <li>هر رزرو فقط برای بازه زمانی ثبت‌شده معتبر است.</li>

          <li>مسئولیت صحت اطلاعات اقامتگاه بر عهده میزبان است.</li>

          <li>کاربر موظف است ظرفیت تعیین‌شده برای اقامتگاه را رعایت کند.</li>

          <li>هرگونه استفاده غیرمجاز یا ثبت اطلاعات نادرست ممکن است منجر به مسدود شدن حساب کاربری شود.</li>

          <li>پناه صرفاً بستری برای ارتباط میان میزبان و متقاضی اسکان است.</li>

          <li>در شرایط اضطراری، اولویت تخصیص اقامتگاه بر اساس سیاست‌های سامانه انجام می‌شود.</li>
        </ol>
      </div>

      <div class="alert alert-light mt-4">
        رعایت قوانین فوق باعث ارائه خدمات بهتر و ایجاد محیطی امن برای تمامی کاربران خواهد شد.
      </div>

    </div>

  </div>
</template>

<script setup>
</script>

<style scoped>
.support-page{min-height:60vh;padding:36px 12px;}
.support-card{
max-width:760px;
background:white;
border:1px solid rgba(72,72,78,.06);
}
.rules-list li{
margin-bottom:12px;
line-height:2;
}
</style>