<template>
<div class="speed d-flex justify-content-center">

    <div class="speed-container">

        <div class="search-box">

            <div class="title text-center mb-5">
                <h3>جستجوی سریع</h3>
                <p>اقامتگاه مناسب خود را سریع پیدا کنید</p>
            </div>

            <div class="row g-4">

                <!-- شهر -->
                <div class="col-md-6 col-lg-3">
                    <div class="card p-3 h-100">

                        <h5>📍 شهر یا استان</h5>

                        <input
                            class="form-control mt-3"
                            v-model="city"
                            placeholder="مثلاً تهران">

                        <button
                            class="btn btn-success mt-3 w-100"
                            @click="searchCity">

                            جستجو

                        </button>

                    </div>
                </div>

                <!-- ظرفیت -->
                <div class="col-md-6 col-lg-3">
                    <div class="card p-3 h-100">

                        <h5>👥 ظرفیت</h5>

                        <select
                            class="form-select mt-3"
                            v-model="capacity">

                            <option value="">انتخاب کنید</option>
                            <option>1</option>
                            <option>2</option>
                            <option>4</option>
                            <option>6</option>
                            <option>8</option>

                        </select>

                        <button
                            class="btn btn-success mt-3 w-100"
                            @click="searchCapacity">

                            جستجو

                        </button>

                    </div>
                </div>

                <!-- سرویس خواب -->
                <div class="col-md-6 col-lg-3">
                    <div class="card p-3 h-100">

                        <h5>🛏 سرویس خواب</h5>

                        <input
                            class="form-control mt-3"
                            v-model="bedService"
                            placeholder="مثلاً تخت">

                        <button
                            class="btn btn-success mt-3 w-100"
                            @click="searchBed">

                            جستجو

                        </button>

                    </div>
                </div>

                <!-- رایگان -->
                <div class="col-md-6 col-lg-3">
                    <div class="card p-3 h-100 d-flex justify-content-center">

                        <h5>💚 اقامتگاه رایگان</h5>

                        <button
                            class="btn btn-success mt-4"
                            @click="searchFree">

                            مشاهده

                        </button>

                    </div>
                </div>

            </div>

        </div>

    </div>

</div>
</template>