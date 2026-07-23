const API_BASE = import.meta.env.VITE_API_BASE_URL || ''

async function request(path, options = {}) {
  const token = localStorage.getItem('access_token')
  const isFormData = options.body instanceof FormData
  const headers = {
    ...(token ? { Authorization: `Bearer ${token}` } : {}),
    ...(options.headers || {}),
  }

  if (!isFormData) {
    headers['Content-Type'] = 'application/json'
  }

  const response = await fetch(`${API_BASE}${path}`, {
    credentials: 'include',
    headers,
    ...options,
  })

  const text = await response.text()
  const data = text ? JSON.parse(text) : null

  if (!response.ok) {
    throw new Error(data?.error || data?.message || response.statusText)
  }
  return data
}

function persistAuthData(data) {
  if (data?.access) {
    localStorage.setItem('access_token', data.access)
  }
  if (data?.profile?.slug) {
    localStorage.setItem('profile_slug', data.profile.slug)
  }
  if (data?.user?.username) {
    localStorage.setItem('user_name', data.user.username)
    console.log(data.user);
    console.log(data.user.user_type);

    
  }
  const role = data?.user?.user_type
   || data?.user?.role || 
   localStorage.getItem('user_role') || 'guest'
  console.log("role=",role)
  localStorage.setItem('user_role', role)
  if (typeof window !== 'undefined') {
    window.dispatchEvent(new Event('auth:changed'))
  }
}

export async function login(username, password) {
  const data = await request('/api/custom-login/', {
    method: 'POST',
    body: JSON.stringify({ username, password }),
  })
  console.log('login response',data);
  
  persistAuthData(data)
  return data
}

export async function register(payload) {
  const data = await request('/api/register/', {
    method: 'POST',
    body: JSON.stringify(payload),
  })
  persistAuthData(data)
  return data
}



export async function createRoomWithImages(payload) {
  const formData = new FormData()

  Object.entries(payload).forEach(([key, value]) => {
    if (value === undefined || value === null) {
      return
    }

    if (Array.isArray(value)) {
      value.forEach(item => {
        formData.append(key, item)
      })
      return
    }

    formData.append(key, value)
  })
  console.log(formData);
  for (const pair of formData.entries()) {
    console.log(pair[0], pair[1]);
  }
  return request('/room/upload-images/', {
    method: 'POST',
    body: formData,
  })
}

export async function fetchRooms(params = '') {
  // Backward compatible: accepts either a plain search string or an object
  // of filters, e.g. { search: 'تهران', capacity: '4', bed_service: 'تخت', price: 'free' }
  const filters = typeof params === 'string' ? { search: params } : (params || {})

  const query = Object.entries(filters)
    .filter(([, value]) => value !== undefined && value !== null && value !== '')
    .map(([key, value]) => `${encodeURIComponent(key)}=${encodeURIComponent(value)}`)
    .join('&')

  return request(`/room/${query ? `?${query}` : ''}`)
}

export async function fetchRoomById(id) {
  return request(`/room/detail/${id}`)
}

export async function updateRoom(id, payload) {
  return request(`/room/detail/${id}`, {
    method: 'PUT',
    body: JSON.stringify(payload),
  })
}

export async function fetchUserProfile() {
  return request('/api/my-profile/')
}

export async function updateUserProfile(payload) {
  return request('/api/my-profile/', {
    method: 'PUT',
    body: payload instanceof FormData ? payload : JSON.stringify(payload),
  })
}

export async function payForRoom(payload) {
  return request('/payment/listPayment/', {
    method: 'POST',
    body: JSON.stringify(payload),
  })
}

export async function fetchReservations(roomId) {
  return request(`/room/${roomId}/reservations/`)
}
export async function fetchMyRooms() {
  return request("/room/my-rooms/");
}
export async function deleteRoom(id) {
  return request(`/room/detail/${id}`, {
    method: "DELETE",
  });
}
export async function fetchMyReservations() {
  return request("/room/my-reservations/");
}