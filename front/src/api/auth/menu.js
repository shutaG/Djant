import request from '@/utils/request'

const api = {
  menu: '/admin/menu/'
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
    url: api.menu + '/' + id + '/',
    method: 'post',
    data: data
  })
}

// 筛选type=menu的菜单
export function getOnlyMenuApi () {
  return request({
    url: api.menu,
    method: 'get',
    params: {
      type: 'menu'
    }
  })
}
