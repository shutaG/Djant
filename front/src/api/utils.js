import request from '@/utils/request'

const api = {
  'uploadkey': 'common/uploadkey'
}

export function getUpKeyApi () {
  console.log('正在upkey')
  return request({
    url: api.uploadkey,
    method: 'get'
  })
}

export function createMenuApi (data) {
  return request({
    url: api.menu,
    method: 'post',
    data: data
  })
}
