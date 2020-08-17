<template>
  <div>
    <a-modal :visible="visible" :userId="userId" title="用户信息" @ok="$emit('createOk')" @cancel="$emit('createCancel')">
      <a-form :form="form" :label-col="{ span: 5 }" :wrapper-col="{ span: 12 }" >
        <a-form-item
          label="头像"
          :wrapper-col="{ span: 12, }"
          class="avatar">
          <a-upload
            name="file"
            list-type="picture-card"
            class="avatar-uploader"
            :show-upload-list="false"
            action="http://up-z2.qiniup.com"
            :data="{token:key}"
            :before-upload="beforeUpload"
            @change="handleChange"

          >
            <img v-if="imageUrl" :src="imageUrl" alt="avatar" />
            <div v-else>
              <a-icon :type="loading ? 'loading' : 'plus'" />
              <div class="ant-upload-text">
                上传头像
              </div>
            </div>
          </a-upload>
          <a-input
            v-show="false"
            v-decorator="['avatar', { rules: [{ required: true, message: '您还未选择头像' }] }]"
          />
        </a-form-item>
        <a-form-item label="用户姓名">
          <a-input
            v-decorator="['first_name', { rules: [{ required: true, message: '您还未填写姓名' }] }]"
          />
        </a-form-item>
        <a-form-item label="用户账号">
          <a-input
            v-decorator="['username', { rules: [{ required: true, message: '您还未填写账号' }] }]"
          />
        </a-form-item>
        <a-form-item label="密码" >
          <a-input-password
            v-decorator="['password', { rules: [{ required: true, message: '您还未填写密码' }] }]"
          />
        </a-form-item>
        <a-form-item label="重复密码" >
          <a-input-password
            v-decorator="['password2', { rules: [{ required: true, message: '请重复密码' }] }]"
          />
        </a-form-item>
        <a-form-item label="邮箱">
          <a-input
            v-decorator="['email', { rules: [{ required: true, message: '您还未填写邮箱' }] }]"
          />
        </a-form-item>
        <a-form-item label="是否启用">
          <a-switch
            checked-children="启用"
            un-checked-children="禁用"
            v-decorator="['is_active', {valuePropName: 'checked', rules: [] }]"
          />
        </a-form-item>
      </a-form>
    </a-modal>

    2222
  </div>
</template>

<script>
import { getBase64 } from '@/utils/djant'
import { getUpKeyApi } from '@/api/utils'

export default {
  name: 'CreateMenu',
  props: {
    visible: {
      type: Boolean,
      default: true
    },
    userId: {
      type: [Number, null],
      default: null
    }
  },
  data () {
    return {
      key: '',
      formLayout: 'horizontal',
      form: this.$form.createForm(this, { name: 'user_form' }),
      loading: false,
      imageUrl: ''
    }
  },
  created () {
    this.getUpkey()
  },
  methods: {
    // 获取七牛云的上传token
    getUpkey () {
      getUpKeyApi().then(res => {
        this.key = res.result
      })
    },
    // 上传中状态的监听
    handleChange (info) {
      if (info.file.status === 'uploading') {
        this.loading = true
        return
      }
      if (info.file.status === 'done') {
        this.form.setFieldsValue({ 'avatar': info.file.response.src })
        this.form.validateFields((err, values) => {
          console.log(err)
          console.log('form', values)
        })
        console.log('form')
        // Get this url from response in real world.
        getBase64(info.file.originFileObj, imageUrl => {
          this.imageUrl = imageUrl
          this.loading = false
        })
      }
    },
    // 上传前的校验
    beforeUpload (file) {
      const isJpgOrPng = file.type === 'image/jpeg' || file.type === 'image/png'
      if (!isJpgOrPng) {
        this.$message.error('亲,只支持jpg、png格式的图片哦')
      }
      const isLt2M = file.size / 1024 / 1024 < 2
      if (!isLt2M) {
        this.$message.error('亲，图片太大了（需要小于2M）')
      }
      return isJpgOrPng && isLt2M
    }

  }

}
</script>

<style lang="less">
  .avatar{
    margin-bottom:0px;

    img{
      width:100%
    }
  }
</style>
