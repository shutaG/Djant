import request from '@/utils/request'

const api = {
  menu: '/user/menu/'
}

export function createMenuApi (data) {
  return request({
    url: api.menu,
    method: 'post',
    data: data
  })
}

export function updateMenuApi (id, data) {
  return request({
    url: api.menu + id + '/',
    method: 'put',
    data: data
  })
}
