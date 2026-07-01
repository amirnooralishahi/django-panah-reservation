// URL API شما
const apiUrl = 'http://127.0.0.1:8000/api-UserList/' // آدرس صحیح API خود را وارد کنید

// // تابع برای دریافت داده‌ها
// async function fetchPassengerList() {
//   try {
//     const response = await fetch(apiUrl, {
//       method: 'GET', // نوع درخواست
//       headers: {
//         'Content-Type': 'application/json', // نوع محتوا
//       },
//     })

//     // بررسی وضعیت پاسخ
//     if (!response.ok) {
//       throw new Error('Network response was not ok')
//     }

//     const data = await response.json() // تبدیل پاسخ به JSON
//     console.log(data) // نمایش داده‌ها در کنسول
//     // اینجا می‌توانید داده‌ها را به دلخواه خود استفاده کنید
//   } catch (error) {
//     console.error('There was a problem with the fetch operation:', error)
//   }
// }

// فراخوانی تابع
// fetchPassengerList()
fetch(apiUrl)
  .then((res) => res.json())
  .then((data) => {
    console.log(data)
    document.getElementById('name').innerText = data[0]['fistname']
  })
