<template class="khgl">
  <div>
    <div>
    <div style="background-color: #3062c7">
      <el-image style="width: 200px; height: 80px" :src="url"></el-image>
      <div style="font-size: 50px; color: #fff; float: right; left: 50%">
        客户签到系统
      </div>
    </div>
    </div>

    <div style="height: 10px"></div>
    <div style="height: 10px">
      <div style="float: left">
        <el-input
          v-model="input"
          placeholder="请输入内容"
          autofocus
          size="small"
          @keyup.enter.native="sousuo"
        ></el-input>
      </div>
      <div style="float: left" class="left-button">
        <el-button size="small" type="info" @click.native="sousuo"
          >编号搜索</el-button
        >
      </div>
      <div style="float: left">
        <el-input
          v-model="input_name"
          placeholder="请输入内容"
          size="small"
          @keyup.enter.native="sousuo_name"
        ></el-input>
      </div>
      <div style="float: left" class="left-button">
        <el-button size="small" type="info" @click.native="sousuo_name"
          >姓名搜索</el-button
        >
      </div>
      <div style="float: left">
        <el-input
          v-model="input_phone"
          placeholder="请输入内容"
          size="small"
          @keyup.enter.native="sousuo_phone"
        ></el-input>
      </div>
      <div style="float: left" class="left-button">
        <el-button size="small" type="info" @click.native="sousuo_phone"
          >电话搜索</el-button
        >
      </div>
      <div style="float: left">
        <el-input
          v-model="input_company"
          placeholder="请输入内容"
          size="small"
          @keyup.enter.native="sousuo_company"
        ></el-input>
      </div>
      <div style="float: left" class="left-button">
        <el-button size="small" type="info" @click.native="sousuo_company"
          >公司搜索</el-button
        >
      </div>
      <div style="float: right" class="right-button">
        <el-button size="small" type="warning" @click.native="shuaxin"
          >刷新</el-button
        >
        <el-button size="small" type="success" @click.native="daoru"
          >批量导入</el-button
        >
        <el-button size="small" type="danger" @click.native="shanchu"
          >删除</el-button
        >
        <el-button
          size="small"
          :loading="downloadLoading"
          type="info"
          icon="el-icon-document"
          @click="exportExcel"
        >
          表格导出
        </el-button>
        <el-button size="small" type="danger" @click.native="jump"
          >抽奖</el-button
        >
      </div>
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
          <el-form-item label="编号" :label-width="formLabelWidth">
            <el-input
              v-model="form.number"
              autocomplete="off"
              disabled
            ></el-input>
          </el-form-item>
          <el-form-item label="姓名" :label-width="formLabelWidth">
            <el-input v-model="form.name" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="电话" :label-width="formLabelWidth">
            <el-input v-model="form.phone" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="企业名称" :label-width="formLabelWidth">
            <el-input v-model="form.company" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="客户经理" :label-width="formLabelWidth">
            <el-input v-model="form.fzr" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="签到状态">
            <el-select v-model="form.qdbz" placeholder="请选签到状态">
              <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              >
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="备注" :label-width="formLabelWidth">
            <el-input v-model="form.bz" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>
        <el-dialog
          width="30%"
          title="确认修改"
          :visible.sync="innerVisible"
          append-to-body
        >
          <div slot="footer" class="dialog-footer">
            <el-button @click="innerVisible = false">取 消</el-button>
            <el-button type="primary" @click.native="xiugai_queren"
              >保存</el-button
            >
          </div>
        </el-dialog>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="innerVisible = true"
            >修改</el-button
          >
        </div>
      </el-dialog>
    </div>
    <div>
      <el-dialog
        title="客户信息增加"
        :visible.sync="dialogFormVisible_1"
        width="50%"
        :before-close="handleClose"
      >
        <!-- <span>{{multipleSelection[0]}}</span> -->
        <el-form :model="form2">
          <el-form-item label="编号" :label-width="formLabelWidth">
            <el-input
              v-model="form2.number"
              autocomplete="off"
              disabled
            ></el-input>
          </el-form-item>
          <el-form-item label="姓名" :label-width="formLabelWidth">
            <el-input v-model="form2.name" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="电话" :label-width="formLabelWidth">
            <el-input v-model="form2.phone" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="企业名称" :label-width="formLabelWidth">
            <el-input v-model="form2.company" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="客户经理" :label-width="formLabelWidth">
            <el-input v-model="form2.fzr" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="备注" :label-width="formLabelWidth">
            <el-input v-model="form2.bz" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>
        <el-dialog
          width="30%"
          title="确认增加"
          :visible.sync="innerVisible_1"
          append-to-body
        >
          <div slot="footer" class="dialog-footer">
            <el-button @click="innerVisible_1 = false">取 消</el-button>
            <el-button type="primary" @click.native="zengjia1_queren"
              >确定</el-button
            >
          </div>
        </el-dialog>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible_1 = false">取 消</el-button>
          <el-button type="primary" @click="innerVisible_1 = true"
            >增加</el-button
          >
        </div>
      </el-dialog>
    </div>
    <div>
      <el-dialog
        title="批量导入表格"
        :visible.sync="dialogFormVisible_zengjia"
        width="50%"
        :before-close="handleClose"
      >
        <div class="title">
          <!-- <div>
            <span style="float: left">单据导入</span>
          </div> -->
          <div style="float: left">
            <el-upload
              class="upload"
              action=""
              :multiple="false"
              :show-file-list="false"
              accept="csv, application/vnd.ms-excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
              :http-request="httpRequest"
            >
              <el-button size="small" type="primary">批量导入</el-button>
            </el-upload>
          </div>
        </div>
        <div class="body" style="margin-right: 10px">
          <el-table
            :data="tableData_daoru"
            height="400"
            stripe
            style="margin-right: 10px"
            @selection-change="handleSelectionChange"
          >
            <el-table-column type="selection" width="55"></el-table-column>
            <el-table-column
              prop="number"
              label="编号"
              width="130"
            ></el-table-column>
            <el-table-column
              prop="name"
              label="姓名"
              width="80"
            ></el-table-column>
            <el-table-column
              prop="phone"
              label="联系方式 "
              width="120"
            ></el-table-column>
            <el-table-column
              prop="company"
              label="企业名"
              width="200"
            ></el-table-column>
            <el-table-column
              prop="fzr"
              label="所属业务经理"
              width="120"
            ></el-table-column>
          </el-table>
        </div>
        <el-dialog
          width="30%"
          title="确认导入"
          :visible.sync="innerVisible_zengjia"
          append-to-body
        >
          <div slot="footer" class="dialog-footer">
            <el-button @click="innerVisible_zengjia = false">取 消</el-button>
            <el-button type="primary" @click.native="daoru_queren"
              >保存</el-button
            >
          </div>
        </el-dialog>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible_zengjia = false"
            >取 消</el-button
          >
          <el-button type="primary" @click="innerVisible_zengjia = true"
            >导入</el-button
          >
        </div>
      </el-dialog>
    </div>
    <div>
      <el-table
        :data="tableData1"
        height="710"
        stripe
        style="width: 100%"
        @selection-change="handleSelectionChange"
      >
        <el-table-column type="selection" width="55"></el-table-column>
        <el-table-column
          prop="number"
          label="编号"
          width="200"
        ></el-table-column>
        <el-table-column prop="name" label="姓名" width="200"></el-table-column>
        <el-table-column
          prop="phone"
          label="联系方式 "
          width="200"
        ></el-table-column>
        <el-table-column
          prop="company"
          label="企业名"
          width="400"
        ></el-table-column>
        <el-table-column
          prop="fzr"
          label="所属业务经理"
          width="120"
        ></el-table-column>
        <el-table-column
          prop="qdbz"
          label="签到状态"
          :formatter="formatter"
          width="100"
        ></el-table-column>
        <el-table-column prop="bz" label="备注" width="400"></el-table-column>
        <el-table-column prop="fzr" label="操作签到" width="200" align="right"
          ><template slot-scope="scope">
            <!-- 　　　　　　<el-button type="text" @click="checkDetail(scope.row.phone)">查看详情</el-button> -->
            　　　　　　<el-button
              type="primary"
              size="mini"
              @click="qiandao(scope.row.qdbz, scope.row.number)"
              >签到</el-button
            >
            　　　　　　<el-button
              type="danger"
              size="mini"
              @click="xiugai(scope.row)"
              >修改</el-button
            >
            　　　　</template
          >
        </el-table-column>
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
    <div
      style="
        height: 60px;
        background-color: #3062c7;
        text-align: center;
        margin-top: 10px;
      "
    >
      <div style="color: #ffffff; margin-top: 10px">
        Copyright@Ted1988 未经授权，网站内容不得转载
      </div>
    </div>
  </div>
</template>
<script type="text/ecmascript-6">
import Axios from "axios";
import XLSX from "xlsx";
export default {
  data() {
    return {
      url: require("@/assets/unnamed.jpg"),
      total1: 0, //客户信息总数
      currentPage1: 1, //初始分页开始页
      pageSize: 10, //初始分页条数
      show: false, //隐藏ID列
      tableData: [], //客户信息总信息获取结果
      tableData1: [], //表格分页后数据
      tableData_daoru: [], //批量导入数据
      multipleSelection: [], //表格勾选数据
      dialogFormVisible: false, //客户修改对话框
      dialogFormVisible_1: false, //客户增加对话框
      innerVisible: false, //客户修改内层对话框
      innerVisible_1: false, //客户增加内层对话框
      dialogFormVisible_zengjia: false, //客户增加对话框
      innerVisible_zengjia: false, //客户增加内层确认对话框
      downloadLoading: false, //表格导出使用
      autoWidth: true, //表格导出使用
      bookType: "xlsx", //表格导出使用
      filename: "", //表格导出使用
      form: {
        //客户修改表单数据
        number: "",
        name: "",
        phone: "",
        company: "",
        fzr: "",
        qdbz: "",
        bz: "",
      },
      form2: {
        //客户增加表单数据
        number: "",
        name: "",
        phone: "",
        company: "",
        fzr: "",
        qdbz: "",
        bz: "",
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
      options: [
        {
          value: "1",
          label: "已签到",
        },
        {
          value: "0",
          label: "未签到",
        },
      ],
      value: "",

      formLabelWidth: "100px", //对话框宽度
      input: "",
      input_name: "",
      input_phone: "",
      input_company: "",
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
        // alert("删除数据失败"+res.data);
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
        alert(err);
        // alert(localStorage.getItem("Authorization"));
        console.log("err", err);
      });
  },
  methods: {
    jump() {
      //通过push进行跳转
      this.$router.push("/home");
    },
    exportExcel() {
      let sourceOriginAmount = this.tableData; // 需要导出的数据，可以动态获取
      this.loading = true; // 设置一个loading，生成Excel需要时间
      import("@/vendor/Export2Excel.js").then((excel) => {
        // 导入js模块
        const tHeader = [
          "编号",
          "姓名",
          "联系方式",
          "公司名称",
          "客户经理",
          "签到状态",
          "备注",
        ]; // 导出excel 的标题
        const filterVal = [
          "number",
          "name",
          "phone",
          "company",
          "fzr",
          "qdbz",
          "bz",
        ]; // 每个标题对应的字段

        const list = (sourceOriginAmount || []).map((item, key) => {
          // 通过 map 方法遍历，组装数据成上面的格式
          return {
            index: key + 1,
            number: item.number,
            name: item.name,
            phone: item.phone,
            company: item.company,
            fzr: item.fzr,
            qdbz: item.qdbz,
            bz: item.bz,
          };
        });

        if (list) {
          const data = this.formatJson(filterVal, list); // 生成json数据
          excel.export_json_to_excel({
            // 调用excel方法生成表格
            header: tHeader,
            data,
            filename: this.goodsName,
          });
        } else {
          alert("暂无无数据");
        }
        this.loading = false;
      });
    },
    formatJson(filterVal, jsonData) {
      return jsonData.map((v) => filterVal.map((j) => v[j]));
    },
    httpRequest(e) {
      //导入表格控制
      let that = this;
      let file = e.file; // 文件信息
      if (!file) {
        // 没有文件
        return false;
      } else if (!/\.(xls|xlsx)$/.test(file.name.toLowerCase())) {
        // 判断是否excel格式
        that.$message.error("上传格式不正确，请上传xls或者xlsx格式");
        return false;
      }
      const fileReader = new FileReader();
      fileReader.onload = (ev) => {
        try {
          const data = ev.target.result;
          const workbook = XLSX.read(data, {
            type: "binary", // 以字符编码的方式解析
          });
          const exlname = workbook.SheetNames[0]; // 取第一张表
          const exl = XLSX.utils.sheet_to_json(workbook.Sheets[exlname]); // 生成json表格内容
          // console.log(exl);
          // 将 JSON 数据挂到 data 里
          this.tableData_daoru = exl;
          console.log(that.tableData_daoru);
          let arr = this.tableData_daoru[0]; //获取json键名
        } catch (e) {
          console.log(e);
          return false;
        }
      };
      fileReader.readAsBinaryString(file);
    },
    shuaxin() {
      //刷新表格
      location.reload();
    },
    xiugai1() {
      //修改用户信息

      if (qdbz == 1) {
        this.$message({
          message: "已经签到了！",
          type: "warning",
        });
      } else {
        const that = this;
        Axios({
          //页面加载成功立即请求所有客户信息数据
          method: "post",
          url: "/research",
          data: { code: "003", number: number },
        })
          .then(function (res) {
            if (res.data["msg"] == "00") {
              that.$message({
                message: "签到成功！",
                offset: 40,
                type: "success",
              });
            } else {
              that.$message.error({
                message: "签到失败！",
                offset: 40,
              });
            }
            //  alert("删除数据失败"+res.data[0]["fzr"]);
            // location.reload();
          })
          .catch(function (err) {
            alert(err);
            // alert(localStorage.getItem("Authorization"));
            console.log("err", err);
          });
      }
    },
    qiandao(qdbz, number) {
      if (qdbz == 1) {
        this.$message({
          message: "已经签到了！",
          type: "warning",
        });
      } else {
        const that = this;
        Axios({
          //页面加载成功立即请求所有客户信息数据
          method: "post",
          url: "/research",
          data: { code: "003", number: number },
        })
          .then(function (res) {
            if (res.data["msg"] == "00") {
              location.reload();
              that.$message({
                message: "签到成功！",
                offset: 40,
                type: "success",
              });
            } else {
              that.$message.error({
                message: "签到失败！",
                offset: 40,
              });
            }
            //  alert("删除数据失败"+res.data[0]["fzr"]);
          })
          .catch(function (err) {
            alert(err);
            // alert(localStorage.getItem("Authorization"));
            console.log("err", err);
          });
      }
    },
    formatter(row, column, cellValue, index) {
      //格式化签到状态
      // row: 行数据
      // column: 列属性
      // cellValue: 单元格数据值
      // index: 行索引，注意：2.3.9版本以后才有。
      // alert(row.qdbz)
      if (row.qdbz == 1) {
        return "已签到";
      } else {
        return "未签到";
      }
    },
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
    xiugai(row) {
      //客户信息修改
      this.dialogFormVisible = true;
      this.form = row;
      this.form.qdbz = row.qdbz + "";
    },
    xiugai_queren() {
      //修改客户信息提交
      if (this.form.name === "") {
        this.$message({
          message: "客户名称不能为空！",
          type: "warning",
        });
      } else {
        // alert(this.form1.clientname);
        //客户信息增加与后台交互
        Axios({
          method: "post",
          url: "/research",
          data: {
            code: "005",
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
            this.form = [];
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
    daoru() {
      //批量导入
      this.tableData_daoru = [];
      //客户信息导入对话框
      this.dialogFormVisible_zengjia = true;
    },
    daoru_queren() {
      if (this.tableData_daoru.length == 0) {
        this.$message({
          message: "未导入任何数据，请检查表格！",
          type: "warning",
        });
      } else {
        // alert(this.form1.clientname);
        //客户信息增加与后台交互
        Axios({
          method: "post",
          url: "/research",
          data: {
            code: "004",
            data: this.tableData_daoru,
          },
        })
          .then(function (res) {
            if (res.data["msg"] == "00") {
              alert("导入成功！");
            } else {
              alert("导入失败！");
            }
            //  alert("删除数据失败"+res.data[0]["fzr"]);
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
    sousuo() {
      //编号搜索
      const that = this;
      if(this.input == ""){
        this.$message({
              message: "编号未填，不可搜索！",
              offset: 40,
              type: "error",
            });
      }else{
        var num = this.input;
      Axios({
        //页面加载成功立即请求所有客户信息数据
        method: "post",
        url: "/research",
        data: { code: "002", number: this.input },
      })
        .then((res) => {
          //  alert("删除数据失败"+res.data[0]["fzr"]);
          that.tableData = res.data;
          that.total1 = res.data.length;
          if (res.data["msg"] == "104") {
            this.$message({
              message: "未检索到记录！",
              offset: 40,
              type: "error",
            });
            that.zengjia1(num);
            // location.reload();
          } else {
            that.tableData1 = [];
            that.tableData1.push(that.tableData[0]);
          }
        })
        .catch((error) => {
          alert(err);
          // alert(localStorage.getItem("Authorization"));
          console.log("err", err);
        });
      this.input = "";
      }
    },
    sousuo_name() {
      //姓名搜索
      const that = this;
      Axios({
        //页面加载成功立即请求所有客户信息数据
        method: "post",
        url: "/research",
        data: { code: "008", name: this.input_name },
      })
        .then((res) => {
          //  alert("删除数据失败"+res.data[0]["fzr"]);
          that.tableData = res.data;
          that.total1 = res.data.length;
          if (res.data["msg"] == "104") {
            this.$message({
              message: "未检索到记录！",
              offset: 40,
              type: "error",
            });
            // location.reload();
          } else {
            that.tableData1 = [];
            // alert(that.tableData1);
            for (let i = 0; i <= 10; ++i) {
              that.tableData1.push(that.tableData[i]);
            }
            this.pageSize = 10;
            this.handleCurrentChange1(this.currentPage1);
          }
        })
        .catch((error) => {
          alert(err);
          // alert(localStorage.getItem("Authorization"));
          console.log("err", err);
        });
      this.input_name = "";
    },
    sousuo_phone() {
      //电话搜索
      const that = this;
      Axios({
        //页面加载成功立即请求所有客户信息数据
        method: "post",
        url: "/research",
        data: { code: "009", phone: this.input_phone },
      })
        .then((res) => {
          //  alert("删除数据失败"+res.data[0]["fzr"]);
          that.tableData = res.data;
          that.total1 = res.data.length;
          if (res.data["msg"] == "104") {
            this.$message({
              message: "未检索到记录！",
              offset: 40,
              type: "error",
            });
            // location.reload();
          } else {
            that.tableData1 = [];
            // alert(that.tableData1);
            for (let i = 0; i <= 10; ++i) {
              that.tableData1.push(that.tableData[i]);
            }
            this.pageSize = 10;
            this.handleCurrentChange1(this.currentPage1);
          }
        })
        .catch((error) => {
          alert(err);
          // alert(localStorage.getItem("Authorization"));
          console.log("err", err);
        });
      this.input_phone = "";
    },
    sousuo_company() {
      //电话搜索
      const that = this;
      Axios({
        //页面加载成功立即请求所有客户信息数据
        method: "post",
        url: "/research",
        data: { code: "010", company: this.input_company },
      })
        .then((res) => {
          //  alert("删除数据失败"+res.data[0]["fzr"]);
          that.tableData = res.data;
          that.total1 = res.data.length;
          if (res.data["msg"] == "104") {
            this.$message({
              message: "未检索到记录！",
              offset: 40,
              type: "error",
            });
            // location.reload();
          } else {
            that.tableData1 = [];
            // alert(that.tableData1);
            for (let i = 0; i <= 10; ++i) {
              that.tableData1.push(that.tableData[i]);
            }
            this.pageSize = 10;
            this.handleCurrentChange1(this.currentPage1);
          }
        })
        .catch((error) => {
          alert(err);
          // alert(localStorage.getItem("Authorization"));
          console.log("err", err);
        });
      this.input_company = "";
    },
    zengjia1(text) {
      // alert(text);
      this.dialogFormVisible_1 = true;
      this.form2.number = text;
    },
    zengjia1_queren() {
      Axios({
        method: "post",
        url: "/research",
        data: {
          code: "007",
          data: this.form2,
        },
      })
        .then(function (res) {
          if (res.data["msg"] == "00") {
            alert("增加成功！");
          } else {
            alert("导入失败！");
          }
          //  alert("删除数据失败"+res.data[0]["fzr"]);
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
      this.form2 = {};
      this.innerVisible_1 = false;
      this.dialogFormVisible_1 = false;
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
              code: "006",
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
<style>
.background {
  margin-top: 10px;
  margin: 1px;
  padding: 1px;
}
.left-button {
  margin-right: 30px;
  padding-right: 30px;
  float: left;
}
.right-button {
  margin-right: 30px;
  padding-right: 30px;
  float: right;
}
</style>