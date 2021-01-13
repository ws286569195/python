<template>
  <div>
    <div class="title">
      <div>
        <span style="float: left;">单据导入</span>
      </div>
      <div style="float: left;">
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
    <div class="body">
      <el-table
      :data="tableData"
      style="width: 100%">
      <el-table-column
        prop="姓名"
        label="姓名"
        width="180">
      </el-table-column>
      <el-table-column
        prop="时间"
        label="时间"
        width="180">
      </el-table-column>
      <el-table-column
        prop="手机号"
        label="手机号">
      </el-table-column>
    </el-table>

    </div>
    <div class="footer">
          <div >
        <el-button type="primary" @click.native="test">保存</el-button>
      </div>
    </div>
  </div>
</template>
<script type="text/ecmascript-6">
import Axios from "axios";
import XLSX from 'xlsx'
export default {
  data() {
    return {
      tableData: [
        {
            date: 1111,
            name: '王小虎',
            address: '上海市普陀区金沙江路 1516 弄'
          },
      ],
    };
  },
  
  methods: {
    httpRequest (e) {
   let that = this;
   let file = e.file // 文件信息
   if (!file) {
     // 没有文件
     return false
   } else if (!/\.(xls|xlsx)$/.test(file.name.toLowerCase())) {
     // 判断是否excel格式
     that.$message.error('上传格式不正确，请上传xls或者xlsx格式');
     return false;
   }
   const fileReader = new FileReader();
   fileReader.onload = (ev) => {
     try {
       const data = ev.target.result;
       const workbook = XLSX.read(data, {
         type: 'binary' // 以字符编码的方式解析
       })
       const exlname = workbook.SheetNames[0] // 取第一张表
       const exl = XLSX.utils.sheet_to_json(workbook.Sheets[exlname]) // 生成json表格内容
       // console.log(exl);
       // 将 JSON 数据挂到 data 里
       this.tableData=exl
       console.log(that.tableData)
       let arr = this.tableData[0];//获取json键名
     } catch (e) {
       console.log(e);
       return false;
     }
   }
  fileReader.readAsBinaryString(file);
 },
    exit() {
      //退出登录，清空token
      localStorage.removeItem("Authorization");
      this.$router.push("/login");
      alert("您已成功退出系统！");
    },
    test() {
      Axios({
        method: "post",
        url: "/protected",
        data: { firstName: "Fred", lastName: "Flintstone" },
      })
        .then(function (res) {
          // alert(localStorage.getItem('Authorization'));
          console.log("res", res);
        })
        .catch(function (err) {
          localStorage.removeItem("Authorization");
          this.$router.push("/login");
          alert("您已成功退出系统！");
          // alert(localStorage.getItem("Authorization"));
          console.log("err", err);
        });
    },
  },
};
</script>
<style>
.title {
  border-style: solid;
  border-width: 1px;
  background-color: #5eabd9;
  height: 100px;
}
.body {
  border-style: solid;
  border-width: 1px;
  background-color: #ffffff;
}
.footer {
  border-style: solid;
  border-width: 1px;
  background-color: #9dafbf;
  height: 80px;
}
</style>