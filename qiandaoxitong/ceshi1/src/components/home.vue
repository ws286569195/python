<template>
  <div>
    <div style="position: absolute" class="background">
      <el-image :src="src" style="width: 100%; height: 100%"></el-image>
    </div>
    <el-carousel :interval="4000" type="card" height="300px">
      <el-carousel-item v-for="item in imagebox" :key="item.id">
        <img :src="item.idView" class="image" />
      </el-carousel-item>
    </el-carousel>
    <div
      style="
        height: 90px;
        width: 200px;
        position: absolute;
        bottom: 2%;
        color: #ffec67;
        right: 0%;
        font-size: 100px;
      "
    >
      <el-image :src="src2" style="width: 100%; height: 100%"></el-image>
    </div>
    <div
      style="
        width: 30px;
        position: absolute;
        top: 300px;
        color: #ffec67;
        left: 20%;
        font-size: 100px;
      "
    >
      {{ text }}
    </div>
    <div
      style="
        width: 30px;
        position: absolute;
        top: 300px;
        color: #ffec67;
        left: 30%;
        font-size: 50px;
      "
    >
      {{ text1 }}
    </div>
    <div
      style="
        position: absolute;
        top: 300px;
        color: #ffec67;
        left: 40%;
        font-size: 100px;
      "
    >
      {{ number }}
    </div>
    <div
      style="
        position: absolute;
        top: 450px;
        color: #ffec67;
        left: 40%;
        font-size: 30px;
      "
    >
      {{ name }}
    </div>
    <div
      style="
        position: absolute;
        top: 500px;
        color: #ffec67;
        left: 40%;
        font-size: 30px;
      "
    >
      {{ company }}
    </div>
    <div style="position: absolute; bottom: 100px; color: #fff; left: 850px">
      <template>
        <el-button
          round
          size="medium"
          type="danger"
          @click="start"
          class="start"
          :disabled="isdisabled_start"
          >抽奖</el-button
        >
        <el-button
          round
          size="medium"
          type="danger"
          @click="stop"
          class="stop"
          :disabled="isdisabled_stop"
          >停止</el-button
        >
      </template>
    </div>
    <div style="position: absolute; top: 10px; left: 5%">
      <audio
        :src="music1"
        class="media-audio"
        loop
        autoplay
        ref="MusicPlay"
      ></audio>
    </div>
    <div style="position: absolute; top: 10px; left: 5%">
      <audio :src="music2" class="media-audio" autoplay ref="MusicPlay"></audio>
    </div>
    <div style="position: absolute; bottom: 10px; color: #fff; left: 10px">
      <template>
        <el-button
          round
          size="small"
          type="danger"
          @click="chongzhi"
          class="start"
          >重置</el-button
        >
        <el-button round size="small" type="info" @click="peizhi" class="stop"
          >配置</el-button
        >
        <el-button
          round
          size="small"
          type="success"
          @click.native="jump"
          class="stop"
          >中奖名单</el-button
        >
        <el-button
          round
          size="small"
          type="warning"
          @click="fanhui"
          class="stop"
          >返回</el-button
        >
      </template>
    </div>
  </div>
</template>
<script>
import Axios from "axios";
export default {
  components: {},
  data() {
    return {
      src: require("@/assets/bg.png"),
      src1: require("@/assets/bg1.jpg"),
      src2: require("@/assets/unnamed.jpg"),
      music1: "",
      music2: "",
      choujiang_music: false,
      tingzhi_music: false,
      tableData: [], //参与人员,
      number: "", //随机号码
      name: "", //随机人名
      company: "", //随机公司名称
      three: 3, //三等奖个数
      two: 2, //二等奖个数
      one: 1, //一等奖个数
      choujiang_count: 0, //抽奖计次
      mingxi: [], //中奖奖明细
      text: "", //中奖说明
      text1: "",
      int: 0, //定时器
      isdisabled_start: false, //抽奖按钮禁止状态
      isdisabled_stop: true, //停止按钮禁止状态
      zhongjiangmingdan: false, //中奖名单
      imagebox: [
        { id: 0, idView: require("@/assets/1.png") },
        { id: 1, idView: require("@/assets/2.png") },
        { id: 2, idView: require("@/assets/3.png") },
        //imagebox是assets下一个放图片的文件夹
      ],
    };
  },
  created: function () {
    const that = this;
    Axios({
      //页面加载成功立即请求所有客户信息数据
      method: "post",
      url: "/choujiang",
      data: { code: "001", msg: "" },
    })
      .then(function (res) {
        // alert("删除数据失败"+res.data);
                that.tableData = res.data;
        if(that.tableData.length >6){

        }else{
          console.log("that.tableData.length", that.tableData.length);
          alert("签到人数不满足抽奖条件,无法抽奖！")
          that.isdisabled_start=true;
        }
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
    chongzhi() {
      this.choujiang_count = 0;
      this.number = "";
      this.name = "";
      this.company = "";
      this.text = "";
      this.text1 = "";
      Axios({
        method: "post",
        url: "/choujiang",
        data: { code: "004", data: "" },
      })
        .then((res) => {
          // alert(res.data["msg"])
          this.$message({
            message: "重置完成！",
            offset: 40,
            type: "success",
          });
        })
        .catch(function (err) {
          // alert("错误"+this.form1);
          // alert(localStorage.getItem("Authorization"));
          console.log("err", err);
        });
    },
    start() {
      this.text = "";
      this.text1 = "";
      this.int = setInterval(this.clock, 50);
      this.isdisabled_start = true;
      this.isdisabled_stop = false;
      this.music1 = require("@/assets/main3.mp3");
      this.music2 = "";
    },
    stop() {
      this.music1 = "";
      this.music2 = require("@/assets/win.mp3");
      clearInterval(this.int);
      this.isdisabled_start = false;
      this.isdisabled_stop = true;
      this.choujiang_count = this.choujiang_count + 1;
      this.tableData.map((val,i) =>{
        if(val["number"] === this.number ){
          console.log(this.tableData[i]["number"])
          this.tableData.splice(i,1);
          console.log(this.tableData.length)
        }
      }

      );
      if (this.choujiang_count <= this.three) {
        // alert(
        //   "完成三等奖第" +
        //     this.choujiang_count +
        //     "轮抽奖，中奖号码为：" +
        //     this.number
        // );
        var item = {};
        item["number"] = this.number;
        item["name"] = this.name;
        item["company"] = this.company;
        item["zjbz"] = "3";
        this.text = "三等奖";
        this.text1 = "第" + this.choujiang_count + "位获奖者";
        this.mingxi.push(item);
      } else {
        if (this.choujiang_count - this.three <= this.two) {
          //   alert(
          //   "完成二等奖第" +
          //     (this.choujiang_count-this.three) +
          //     "轮抽奖，中奖号码为：" +
          //     this.number
          // );
          var item = {};
          item["number"] = this.number;
          item["name"] = this.name;
          item["company"] = this.company;
          item["zjbz"] = "2";
          this.text = "二等奖";
          this.text1 = "第" + (this.choujiang_count - this.three) + "位获奖者";
          this.mingxi.push(item);
        } else {
          if (this.choujiang_count - this.three - this.two <= this.one) {
            var item = {};
            item["number"] = this.number;
            item["name"] = this.name;
            item["company"] = this.company;
            item["zjbz"] = "1";
            this.text = "一等奖";
            this.text1 =
              "第" +
              (this.choujiang_count - this.three - this.two) +
              "位获奖者";
            this.mingxi.push(item);
            this.isdisabled_start = true;
            // alert("完成所有奖项抽取！");
            Axios({
              method: "post",
              url: "/choujiang",
              data: { code: "002", data: this.mingxi },
            })
              .then((res) => {
                // alert(res.data["msg"])
                this.$message({
                  message: "完成奖项抽取，并上传结果！",
                  offset: 40,
                  type: "success",
                });
              })
              .catch(function (err) {
                // alert("错误"+this.form1);
                // alert(localStorage.getItem("Authorization"));
                console.log("err", err);
              });
          }
        }
      }
    },
    clock() {
      var item = this.tableData[
        Math.floor(Math.random() * this.tableData.length)
      ];
      this.number = item["number"];
      this.name = "姓名：" + item["name"];
      this.company = "公司名称:" + item["company"];
    },
    jump() {
      // this.$router.push("/zjmd");
      this.$router.push({name: 'zjmd', params: {data: this.mingxi}})
    },
    peizhi() {},
    fanhui() {
      this.$router.push("/khgl");
    },
  },
};
</script>

<style>
.background {
  position: absolute;
  width: 100%;
  height: 100%; /**宽高100%是为了图片铺满屏幕 */

  margin: 0px;
  padding: 0px;
}

.front {
  z-index: 1;
  position: absolute;
}

.carousel_image_type {
  width: 100%;
}
</style>