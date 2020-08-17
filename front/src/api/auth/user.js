import request from '@/utils/request'

const api = {
  user: '/admin/user/'
}

export function ListUserApi (data) {
  return request({
    url: api.user,
    method: 'get'
  })
}

export function CreateUserApi (data) {
  return request({
    url: api.user,
    method: 'post',
    data: data
  })
}

export function UpdateUserApi (id, data) {
  return request({
    url: api.user + id + '/',
    method: 'patch',
    data: data
  })
}
