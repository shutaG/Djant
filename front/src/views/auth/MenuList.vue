<template>
  <a-card :bordered="false">
    <div class="create">
      <a-button
        class="btn"
        @click="addMenu"
        type="primary"
        icon="plus">添加</a-button>
    </div>

    <!-- <div @click="addMenu">11112</div> -->
    <a-table :rowKey="(record) => record.id" :columns="menuColumns" :data-source="menuTree" >
      <template slot="icon" slot-scope="row">
        <a-icon :type="row.meta.icon" v-if="row.meta.icon"/> {{ row.meta.icon }}
      </template>
      <template slot="type" slot-scope="row">
        <a-tag color="#87d068" v-if="row.meta.type=='menu'">目录</a-tag>
        <a-tag color="#108ee9" v-if="row.meta.type=='permission'">权限</a-tag>
      </template>
      <template slot="statu" slot-scope="row">
        <a-switch checked-children="显示" un-checked-children="隐藏" :default-checked="row.meta.statu == 'show'" />
      </template>
      <template slot="action" slot-scope="row">
        <a-button
          class="btn-edit"
          type="primary"
          :data-id="row.id"
          size="small"
          icon="edit"
          @click="updateMenu(row)"> 编辑 </a-button>
        <a-button type="danger" :data-id="row.id" size="small" icon="delete"> 删除 </a-button>
      </template>
    </a-table>
    <create-menu
      ref="createMenu"
      :visible="formVisible"
      :pMenu="pMenu"
      @createOk="submit"
      @createCancel="close"
    ></create-menu>
  </a-card>
</template>

<script>
import STree from '@/components/Tree/Tree'
import { STable } from '@/components'
import OrgModal from './modules/OrgModal'
import { getOrgTree, getServiceList } from '@/api/manage'
import { createMenuApi, updateMenuApi } from '@/api/auth/menu'
import { getCurrentUserNav } from '@/api/login'
import CreateMenu from './modules/CreateMenu'
import { getOnlyMenuApi } from '@/api/auth/menu.js'

export default {
  name: 'TreeList',
  components: {
    STable,
    STree,
    OrgModal,
    CreateMenu
  },
  data () {
    return {
      openKeys: ['key-01'],

      // 查询参数
      queryParam: {},
      // 表头
      menuColumns: [
        {
          title: '菜单名称',
          dataIndex: 'meta.title'
        },
        {
          title: '图标',
          scopedSlots: { customRender: 'icon' }
        },
        {
          title: '类型',
          scopedSlots: { customRender: 'type' }
        },
        {
          title: '状态',
          scopedSlots: { customRender: 'statu' }
        },
        {
          title: '权限',
          width: '30%',
          scopedSlots: { customRender: 'icon' }
        },
        {
          title: '操作',
          scopedSlots: { customRender: 'action' }
        }
      ],
      // 加载数据方法 必须为 Promise 对象
      loadData: parameter => {
        return getServiceList(Object.assign(parameter, this.queryParam))
          .then(res => {
            return res.result
          })
      },
      menuTree: [],
      orgTree: [],
      selectedRowKeys: [],
      selectedRows: [],
      formVisible: true,
      editMenuId: null,
      pMenu: []
    }
  },
  created () {
    getOrgTree().then(res => {
      this.orgTree = res.result
    })
    getCurrentUserNav().then(res => {
      console.log('tree', res)
      const menu = []
      this.treeToList(res.result, menu, 0)
      console.log('menu', menu)
      this.menuTree = menu
    })
  },
  methods: {
    // 获取菜单列表
    getMenu () {
      getOnlyMenuApi().then(res => {
        console.log(res)
        this.pMenu = this.treeToList(res)
      })
    },

    treeToList (menu, pid = null, re = [], cha = '|-') {
      console.log('pid', pid)
      for (var item in menu) {
        console.log('item1', menu[item])
        if (menu[item].pid === pid) {
           console.log('item2', menu[item])
           console.log(menu[item].id)
           var re2 = {
             id: menu[item].id,
             title: cha + menu[item].title
           }
           re.push(re2)
           re = this.treeToList(menu, menu[item].id, re, cha + '--')
        }
      }
      console.log('re', re)
      return re
    },

    // 将菜单转为列表

    addMenu () {
      this.getMenu()
      this.formVisible = true
    },
    submit () {
      console.log('submit')
      this.$refs.createMenu.form.validateFields((err, values) => {
        if (!err) {
          console.log(values)
          this.confirmLoading = true
          const promise = this.editMenuId === null ? createMenuApi(values) : updateMenuApi(this.selected, values)
          const hide = this.$message.loading('执行中..', 0)
          promise.then(res => {
            this.$message.success(this.selected === null ? '添加成功！' : '更新成功！')
            this.refreshTable()
            this.close()
            this.$store.dispatch('ReloadRouters')
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
      console.log('close')
      this.formVisible = false
    },
    updateMenu (row) {
      this.formVisible = true
      this.$nextTick(() => {
        this.$refs.createMenu.form.setFieldsValue({
          type: row.meta.type,
          title: row.meta.title,
          component: row.component,
          icon: row.meta.icon,
          statu: row.meta.statu
        })
      }
      )
    },
    handleClick (e) {
      console.log('handleClick', e)
      this.queryParam = {
        key: e.key
      }
      this.$refs.table.refresh(true)
    },
    handleAdd (item) {
      console.log('add button, item', item)
      this.$message.info(`提示：你点了 ${item.key} - ${item.title} `)
      this.$refs.modal.add(item.key)
    },
    handleTitleClick (item) {
      console.log('handleTitleClick', item)
    },
    titleClick (e) {
      console.log('titleClick', e)
    },
    handleSaveOk () {

    },
    handleSaveClose () {

    },

    onSelectChange (selectedRowKeys, selectedRows) {
      this.selectedRowKeys = selectedRowKeys
      this.selectedRows = selectedRows
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
  .custom-tree {

    // /deep/ .ant-menu-item-group-title {
    //   position: relative;
    //   &:hover {
    //     .btn {
    //       display: block;
    //     }
    //   }
    // }

    // /deep/ .ant-menu-item {
    //   &:hover {
    //     .btn {
    //       display: block;
    //     }
    //   }
    // }

    // /deep/ .btn {
    //   display: none;
    //   position: absolute;
    //   top: 0;
    //   right: 10px;
    //   width: 20px;
    //   height: 40px;
    //   line-height: 40px;
    //   z-index: 1050;

    //   &:hover {
    //     transform: scale(1.2);
    //     transition: 0.5s all;
    //   }
    // }
  }
</style>
