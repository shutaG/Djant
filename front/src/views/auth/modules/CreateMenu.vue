<template>
  <div>
    <a-modal :visible="visible" title="Basic Modal" @ok="$emit('createOk')" @cancel="$emit('createCancel')">
      <a-form :form="form" :label-col="{ span: 5 }" :wrapper-col="{ span: 12 }" @submit="handleSubmit">
        <a-form-item label="添加的类型">
          <a-radio-group button-style="solid" v-decorator="['type', { rules: [{ required: true, message: '您想添加菜单还是权限？' }] }]">
            <a-radio-button value="menu">
              菜单
            </a-radio-button>
            <a-radio-button value="permission">
              权限
            </a-radio-button>
          </a-radio-group>
        </a-form-item>
        <a-form-item label="名称">
          <a-input
            v-decorator="['title', { rules: [{ required: true, message: '您还未填写标题' }] }]"
          />
        </a-form-item>
        <a-form-item label="访问路径">
          <a-input
            v-decorator="['path', { rules: [{ required: true, message: '您还未填写访问路径' }] }]"
          />
        </a-form-item>
        <a-form-item label="父级菜单">
          <a-select
            v-decorator="[
              'pid',
              { rules: [{ required: true, message: '添加菜单时，必须选择父级菜单' }] },
            ]"
            placeholder="选择父级菜单"
          >
            <a-select-option v-for="item in pMenu" :key="item.id">
              {{ item.title }}
            </a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item label="组件">
          <a-select
            v-decorator="[
              'component',
              { rules: [{ required: true, message: '添加菜单时，必须要选择跳转的组件' }] },
            ]"
            placeholder="选择跳转的组件"
          >
            <a-select-option v-for="item in userComponents" :key="item">
              {{ item }}
            </a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item label="是否显示">
          <a-switch
            default-checked
            checked-children="显示"
            un-checked-children="隐藏"
            v-decorator="['statu', { rules: [{ required: false, message: 'Please input your note!' }] }]"
          />
        </a-form-item>
        <a-form-item
          label="
            图标代号"
          :wrapper-col="{ span: 5, }">
          <a-row :gutter="1">
            <a-col :span="24">
              <a-input
                v-decorator="['icon', { rules: [{ required: false, message: 'Please input your note!' }] }]"
              />
            </a-col>
            <a-col :span="0"></a-col>
          </a-row>
          </a-switch></a-form-item>
      </a-form>
    </a-modal>

    2222
  </div>
</template>

<script>
import { userComponents } from '@/router/generator-routers.js'

export default {
  name: 'CreateMenu',
  props: {
    visible: {
      type: Boolean,
      default: true
    },
    pMenu: {
      type: Array,
      default: () => {
        return []
      }
    }
  },
  data () {
    return {
      formLayout: 'horizontal',
      form: this.$form.createForm(this, { name: 'permission_from' }),
      userComponents: userComponents
    }
  },
  created () {
     this.getComponents()
  },
  methods: {
    // 对模板列表进行排序
    getComponents () {
      let arr = Object.keys(userComponents)
      arr = Array.from(new	Set(arr))
      arr = arr.sort()
      this.userComponents = arr
    },

    handleSubmit () {
      console.log('submit!', this.form)
    }
  }

}
</script>

<style>
</style>
