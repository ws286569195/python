<template>
  <div class="hello">
    <!-- <img src="../../assets/back.jpg" height="609" width="960"> -->
    <div z-index:-1 style="position: relative;height: 10000px;width: 720px;">
      <el-image :src="src" style="height: 520px;width: 720px;"></el-image>
    </div>
    <div id="app1" class="app1">
      <el-form ref="loginForm" :model="loginForm"  label-width="80px">
        <el-form-item  label="账号：" class="form">
          <div class="form-username">
            <el-input v-model="loginForm.username" style="width:200px"></el-input>
          </div>
        </el-form-item>
        <el-form-item label="密码："class="form">
          <div class="form-username">
            <el-input v-model="loginForm.password" type="password" style="width:200px"></el-input>
          </div>
        </el-form-item>
        <el-form-item>
          <div class="form-username">
            <el-button type="primary" @click="login()">登录</el-button>
            <el-button>取消</el-button>
          </div>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template> 
<script>
import axios from "axios";
import { mapMutations } from "vuex";
export default {
  name: "login",
  data() {
    return {
      src: require('@/assets/login.jpg'),
      loginForm: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    onSubmit: function () {
      alert("提交数据！");
    },
    ...mapMutations(["changeLogin"]),
    login() {
      let _this = this;

      /////判读账号密码是否输入，没有则alert 出来
      if (this.loginForm.username === "" || this.loginForm.password === "") {
        this.$message({
          message: '账号或密码不能为空！',
          type: 'warning'
        });
      } else {
        // alert(_this.loginForm['username'])
        axios({
          method: "post",
          url: "/api/login",
          data: _this.loginForm,
        })
          .then((res) => {
            console.log(res.data);
            _this.userToken = res.data["access_token"];

            // 将用户token保存到vuex中
            _this.changeLogin({
              Authorization: _this.userToken,
            });
            _this.$router.push("/home");
            this.$message({
                message: "登录成功！",
                offset: 40,
                type: "success",
              });
          })
          .catch((error) => {
            this.$message.error({
                message: "账号或密码错误！",
                offset: 40,
              });
            console.log(error);
          });
      }
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.form-username {
  text-align: left;
}
.app1 {
  position: absolute;
  top: 40%;
  left: 40%;
  margin-left: -50px;
  margin-top: -50px;
  
}

.hello{
  margin-top: 100px;
}
</style>
