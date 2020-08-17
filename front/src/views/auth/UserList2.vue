<template>
  <a-card :bordered="false">
    <div class="create">
      <a-button
        class="btn"
        @click="addUser"
        type="primary"
        icon="plus"
        pagination="false">添加3</a-button>
    </div>
    <a-table ref="table" :columns="columns" :data-source="loadData" :rowKey="(record) => record.id">
      <a-row slot="expandedRowRender" slot-scope="record" style="margin: 0;">
        <a-col :span="8">电话号码：{{ record.tel }}</a-col>
        <a-col :span="8">邮箱：{{ record.email }}</a-col>
      </a-row>
      <template slot="status" slot-scope="row">
        <a-switch checked-children="启用" un-checked-children="禁用" :default-checked="row.is_active == true" />
      </template>
      <template slot="action" slot-scope="row">
        <a-button
          class="btn-edit"
          type="primary"
          :data-id="row.id"
          size="small"
          icon="edit"
          @click="updateUser(row)"> 编辑 </a-button>
        <a-button type="danger" :data-id="row.id" size="small" icon="delete" @click="deleteUser(row.id)"> 删除 </a-button>
      </template>
    </a-table>
    <create-user
      ref="createUser"
      :userId="selected"
      :visible="formVisible"
      @createOk="submit"
      @createCancel="close">

    </create-user>
    </a-table></a-card>
</template>

<script>
import { ListUserApi, CreateUserApi, UpdateUserApi } from '@/api/auth/user'
import CreateUser from './modules/CreateUser'
export default {
  name: 'TreeList',
  components: {
    CreateUser
  },
  data () {
    return {
      // 表头
      columns: [
        {
          title: '姓名',
          dataIndex: 'first_name'
        },
        {
          title: '账号',
          dataIndex: 'username'
        },
        {
          title: '角色',
          scopedSlots: { customRender: 'type' }
        },
        {
          title: '是否启用',
          scopedSlots: { customRender: 'status' }
        },
        {
          title: '操作',
          scopedSlots: { customRender: 'action' }
        }
      ],
      loadData: null,
      formVisible: false,
      selected: null
    }
  },
  created () {
    this.getUserList()
  },
  methods: {
    getUserList () {
      ListUserApi()
        .then(res => {
          this.loadData = res
          // this.$refs.table.refresh()
        })
    },
    updateUser (row) {
      this.formVisible = true
      this.selected = row.id
      const data = {
          avatar: row.avatar,
          first_name: row.first_name,
          username: row.username,
          email: row.email,
          is_active: row.is_active
        }
        console.log(data)
      this.$nextTick(() => {
        this.$refs.createUser.form.setFieldsValue(data)
      }
      )
    },
    // 添加用户信息
    addUser () {
      this.selected = null
      this.formVisible = true
    },
    // 点击确定编辑或提交的按钮
    submit () {
      console.log('submit')
      this.$refs.createUser.form.validateFields((err, values) => {
        console.log(values)
        console.log(err)
        if (!err) {
          console.log(values)
          this.confirmLoading = true
          const promise = this.selected === null ? CreateUserApi(values) : UpdateUserApi(this.selected, values)
          const hide = this.$message.loading('执行中..', 0)
          promise.then(res => {
            this.$message.success(this.selected === null ? '添加成功！' : '更新成功！')
            this.loadData = null
            this.getUserList()
            this.close()
          }).finally(() => {
            hide()
            this.confirmLoading = false
          })
        } else {
          console.log(err)
        }
      })
      // this.formVisible = false
    },
    close () {
      this.formVisible = false
    },
    deleteUser (id) {

    }
  }
}
</script>

<style lang="less">
  .create{
    position: relative;
    height:50px;
    .btn{
      float: right;
    }
  }
  .btn-edit{
    margin-right: 10px;
  }

</style>
