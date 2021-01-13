<template>
  <div>
    <div style="hight: 20px;text-align: left;">
      <!-- <span>客户管理{{multipleSelection}}</span> -->
    </div>
    <div style="float: right;">
      <el-button size="small" type="primary" @click.native="zengjia">增加</el-button>
      <el-button size="small" type="primary" @click.native="xiugai">修改</el-button>
      <el-button size="small" type="primary" @click.native="shanchu">删除</el-button>
    </div>
    <div>
      <el-dialog
        title="客户信息修改"
        :visible.sync="dialogFormVisible"
        width="50%"
        :before-close="handleClose"
      >
        <!-- <span>{{multipleSelection[0]}}</span> -->
        <el-form :model="form">
          <el-form-item label="id" :label-width="formLabelWidth" v-if="show">
            <el-input v-model="form.ID" autocomplete="off" :disabled="true"></el-input>
          </el-form-item>
          <el-form-item label="客户名称" :label-width="formLabelWidth">
            <el-input v-model="form.clientname" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="客户税号" :label-width="formLabelWidth">
            <el-input v-model="form.clienttax" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="地址" :label-width="formLabelWidth">
            <el-input v-model="form.clientaddress" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="电话" :label-width="formLabelWidth">
            <el-input v-model="form.clientphone" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="银行名称" :label-width="formLabelWidth">
            <el-input v-model="form.clientbank" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="银行账号" :label-width="formLabelWidth">
            <el-input v-model="form.clientbankno" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>
        <el-dialog width="30%" title="确认保存" :visible.sync="innerVisible" append-to-body>
          <div slot="footer" class="dialog-footer">
            <el-button @click="innerVisible = false">取 消</el-button>
            <el-button type="primary" @click="dialogFormVisible = false,innerVisible = false">保存</el-button>
          </div>
        </el-dialog>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible = false">取 消</el-button>
          <el-button type="primary" @click.native="xiugai_queren">修改</el-button>
        </div>
      </el-dialog>
    </div>
    <div>
      <el-dialog
        title="客户信息增加"
        :visible.sync="dialogFormVisible_zengjia"
        width="50%"
        :before-close="handleClose"
      >
        <!-- <span>{{multipleSelection[0]}}</span> -->
        <el-form :model="form1">
          <el-form-item label="id" :label-width="formLabelWidth" v-if="show">
            <el-input v-model="form1.ID" autocomplete="off" :disabled="true"></el-input>
          </el-form-item>
          <el-form-item label="客户名称" :label-width="formLabelWidth">
            <el-input v-model="form1.clientname" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="客户税号" :label-width="formLabelWidth">
            <el-input v-model="form1.clienttax" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="地址" :label-width="formLabelWidth">
            <el-input v-model="form1.clientaddress" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="电话" :label-width="formLabelWidth">
            <el-input v-model="form1.clientphone" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="银行名称" :label-width="formLabelWidth">
            <el-input v-model="form1.clientbank" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="银行账号" :label-width="formLabelWidth">
            <el-input v-model="form1.clientbankno" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>
        <el-dialog width="30%" title="确认保存" :visible.sync="innerVisible_zengjia" append-to-body>
          <div slot="footer" class="dialog-footer">
            <el-button @click="innerVisible_zengjia = false">取 消</el-button>
            <el-button type="primary" @click.native="zengjia_queren">保存</el-button>
          </div>
        </el-dialog>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible_zengjia = false">取 消</el-button>
          <el-button type="primary" @click="innerVisible_zengjia = true">增加</el-button>
        </div>
      </el-dialog>
    </div>
    <div>
      <el-table
        :data="tableData1"
        height="710"
        style="width: 100%"
        @selection-change="handleSelectionChange"
      >
        <el-table-column type="selection" width="55"></el-table-column>
        <el-table-column v-if="show" prop="id" label="id" width="180"></el-table-column>
        <el-table-column prop="clientname" label="企业名称" width="180"></el-table-column>
        <el-table-column prop="clienttax" label="企业税号" width="180"></el-table-column>
        <el-table-column prop="clientaddress" label="企业地址" width="180"></el-table-column>
        <el-table-column prop="clientphone" label="电话" width="180"></el-table-column>
        <el-table-column prop="clientbank" label="企业银行" width="180"></el-table-column>
        <el-table-column prop="clientbankno" label="银行账号"></el-table-column>
      </el-table>
    </div>
    <div class="paginationClass">
      <el-pagination
        @size-change="handleSizeChange1"
        @current-change="handleCurrentChange1"
        :current-page="currentPage1"
        :page-sizes="[10, 20, 50, 100]"
        :page-size="pageSize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total1"
      ></el-pagination>
    </div>
  </div>
</template>
<script type="text/ecmascript-6">
import Axios from "axios";
export default {
  data() {
    return {
      total1: 0, //客户信息总数
      currentPage1: 1, //初始分页开始页
      pageSize: 10, //初始分页条数
      show: false, //隐藏ID列
      tableData: [], //客户信息总信息获取结果
      tableData1: [], //表格分页后数据
      multipleSelection: [], //表格勾选数据
      dialogFormVisible: false, //客户修改对话框
      innerVisible: false, //客户修改内层对话框
      dialogFormVisible_zengjia: false, //客户增加对话框
      innerVisible_zengjia: false, //客户增加内层确认对话框
      form: {
        //客户修改表单数据
        ID: "",
        clientname: "",
        clienttax: "",
        clientaddress: "",
        clientphone: "",
        clientbank: "",
        clientbankno: "",
      },
      form1: {
        //客户增加表单数据
        ID: "",
        clientname: "",
        clienttax: "",
        clientaddress: "",
        clientphone: "",
        clientbank: "",
        clientbankno: "",
      },
      formLabelWidth: "100px", //对话框宽度
    };
  },
  created: function () {
    const that = this;
    Axios({
      //页面加载成功立即请求所有客户信息数据
      method: "post",
      url: "/research",
      data: { code: "001", msg: "" },
    })
      .then(function (res) {
        that.tableData = res.data;
        that.total1 = res.data.length;
        for (let i = 0; i <= 10; ++i) {
          that.tableData1.push(that.tableData[i]);
        }
        console.log(that.tableData1);
        console.log(that.total1);
        // alert(localStorage.getItem('Authorization'));
        console.log("that.tableData", that.tableData);
      })
      .catch(function (err) {
        // alert(localStorage.getItem("Authorization"));
        console.log("err", err);
      });
  },
  methods: {
    toggleSelection(rows) {
      //取消选择方法， 暂未使用
      if (rows) {
        rows.forEach((row) => {
          this.$refs.multipleTable.toggleRowSelection(row);
        });
      } else {
        this.$refs.multipleTable.clearSelection();
      }
    },
    handleSelectionChange(val) {
      //表格选择数据
      this.multipleSelection = val;
    },
    handleClose(done) {
      //对话框关闭前统一确认
      this.$confirm("确认关闭？")
        .then((_) => {
          done();
        })
        .catch((_) => {});
    },
    xiugai() {
      //客户信息修改
      if (this.multipleSelection.length != 1) {
        this.$message({
          message: '请选择一条数据！',
          type: 'warning'
        });
      } else {
        this.dialogFormVisible = true;
        this.form = this.multipleSelection[0];
      }
    },
    xiugai_queren() {
      //修改客户信息提交
      if (this.form.clientname === "") {
        this.$message({
          message: '客户名称不能为空！',
          type: 'warning'
        });
      } else {
        // alert(this.form1.clientname);
        //客户信息增加与后台交互
        Axios({
          method: "post",
          url: "/research",
          data: {
            code: "004",
            data: this.form,
          },
        })
          .then((res) => {
            // alert(res.data["msg"])
            this.$message({
              message: "修改成功！",
              offset: 40,
              type: "success",
            });
            location.reload();
          })
          .catch(function (err) {
            // alert("错误"+this.form1);
            // alert(localStorage.getItem("Authorization"));
            console.log("err", err);
          });
        this.form = {};
        this.innerVisible = false;
        this.dialogFormVisible = false;
      }
    },
    zengjia() {
      //客户信息增加对话框
      this.dialogFormVisible_zengjia = true;
    },
    zengjia_queren() {
      if (this.form1.clientname === "") {
        this.$message({
          message: '客户名称不能为空！',
          type: 'warning'
        });
      } else {
        // alert(this.form1.clientname);
        //客户信息增加与后台交互
        Axios({
          method: "post",
          url: "/research",
          data: {
            code: "002",
            data: this.form1,
          },
        })
          .then((res) => {
            this.$message({
              message: "增加成功！",
              offset: 40,
              type: "success",
            });
            location.reload();
          })
          .catch(function (err) {
            this.$message.error({
                message: "增加失败！",
                offset: 40,
              });
            // alert("错误"+this.form1);
            // alert(localStorage.getItem("Authorization"));
            console.log("err", err);
          });
        this.form1 = {};
        this.innerVisible_zengjia = false;
        this.dialogFormVisible_zengjia = false;
      }
    },
    shanchu() {
      //删除选择客户信息
      if (this.multipleSelection.length == 0) {
        alert("请选择一条数据！");
      } else {
        var r = confirm("是否确认删除选择数据");
        if (r == true) {
          Axios({
            method: "post",
            url: "/research",
            data: {
              code: "003",
              data: this.multipleSelection,
            },
          })
            .then((res) => {
              this.$message({
                message: "删除成功！",
                offset: 40,
                type: "success",
              });
              // alert(res.data["msg"]);
              location.reload();
            })
            .catch(function (err) {
              // alert("错误"+this.form1);
              // alert(localStorage.getItem("Authorization"));
              console.log("err", err);
              this.$message.error({
                message: "删除失败！",
                offset: 40,
              });
              // alert("删除数据失败");
            });
        } else {
          // this.$message.error({
          //   message: "删除失败！",
          //   offset: 40,
          // });
          // alert("删除数据失败");
        }
      }
    },
    handleSizeChange1: function (pageSize) {
      // 每页条数切换
      this.pageSize = pageSize;
      this.handleCurrentChange1(this.currentPage1);
    },
    handleCurrentChange1: function (currentPage) {
      //页码切换
      this.currentPage1 = currentPage;
      this.currentChangePage(this.tableData, currentPage);
    },
    //分页方法（重点）
    currentChangePage(list, currentPage) {
      let from = (currentPage - 1) * this.pageSize;
      let to = currentPage * this.pageSize;
      this.tableData1 = [];
      for (; from < to; from++) {
        if (list[from]) {
          this.tableData1.push(list[from]);
        }
      }
    },
  },
};
</script>