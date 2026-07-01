const API_BASE = import.meta.env.VITE_API_BASE_URL || ''

async function request(path, options = {}) {
  const token = localStorage.getItem('access_token')
  const response = await fetch(`${API_BASE}${path}`, {
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
      ...(options.headers || {}),
    },
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
  }
  const role = data?.user?.user_type || data?.user?.role || localStorage.getItem('user_role') || 'guest'
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

export async function sendHostRequest(payload) {
  return request('/api/host-request/', {
    method: 'POST',
    body: JSON.stringify(payload),
  })
}

export async function fetchRooms(search = '') {
  const query = search ? `?search=${encodeURIComponent(search)}` : ''
  return request(`/room/${query}`)
}

export async function fetchRoomById(id) {
  return request(`/room/detail/${id}`)
}

export async function fetchUserProfile() {
  return request('/api/my-profile/')
}

export async function updateUserProfile(payload) {
  return request('/api/my-profile/', {
    method: 'PUT',
    body: JSON.stringify(payload),
  })
}

export async function payForRoom(payload) {
  return request('/payment/listPayment/', {
    method: 'POST',
    body: JSON.stringify(payload),
  })
}
