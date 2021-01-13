<template>
  <div>
    <div style="position: absolute" class="background">
      <el-image :src="src1" style="width: 100%; height: 100%"></el-image>
    </div>
    <div style="position: absolute; top: 10px; left: 5%">
      <audio
        :src="music"
        class="media-audio"
        loop
        autoplay
        ref="MusicPlay"
      ></audio>
    </div>
    <div style="position: absolute; top: 10px; left: 5%">
      <el-image :src="lihua" style="width: 100%; height: 100%"></el-image>
    </div>
    <div style="position: absolute; top: 10px; left: 60%">
      <el-image :src="lihua" style="width: 100%; height: 100%"></el-image>
    </div>
    <div style="position: absolute; top: 500px; left: 10%">
      <el-image :src="lihua1" style="width: 100%; height: 100%"></el-image>
    </div>
    <div style="position: absolute; top: 500px; left: 70%">
      <el-image :src="lihua1" style="width: 100%; height: 100%"></el-image>
    </div>
    <div
      style="
        width: 1900px;
        position: absolute;
        top: 10px;
        color: #ffec67;
        font-size: 100px;
        text-align: center;
      "
    >
      一等奖
    </div>
    <div
      style="
        width: 1850px;
        position: absolute;
        top: 120px;
        color: #ffec67;
        font-size: 50px;
        text-align: center;
      "
    >
      <ul id="example-1" style="list-style: none">
        <li v-for="item in one" :key="item.number">
          {{ item.name }}
        </li>
      </ul>
    </div>
    <div
      style="
        width: 1900px;
        position: absolute;
        top: 320px;
        color: #ffec67;
        font-size: 70px;
        text-align: center;
      "
    >
      二等奖
    </div>
    <div
      style="
        width: 1850px;
        position: absolute;
        top: 400px;
        color: #ffec67;
        font-size: 40px;
        text-align: center;
      "
    >
      <ul id="example-1" style="list-style: none">
        <li v-for="item in two" :key="item.number">
          {{ item.name }}
        </li>
      </ul>
    </div>
    <div
      style="
        width: 1900px;
        position: absolute;
        top: 600px;
        color: #ffec67;
        font-size: 50px;
        text-align: center;
      "
    >
      三等奖
    </div>
    <div
      style="
        width: 1850px;
        position: absolute;
        top: 650px;
        color: #ffec67;
        font-size: 30px;
        text-align: center;
      "
    >
      <ul id="example-1" style="list-style: none">
        <li v-for="item in three" :key="item.number">
          {{ item.name }}
        </li>
      </ul>
    </div>
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
    <div style="position: absolute; bottom: 10px; color: #fff; left: 10px">
      <template>
        <el-button round size="small" type="danger" @click="jump" class="start"
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
      src1: require("@/assets/bg.png"),
      src2: require("@/assets/unnamed.jpg"),
      lihua: require("@/assets/lihua5.gif"),
      lihua1: require("@/assets/lihua3.gif"),
      caizhi: require("@/assets/caizhi.gif"),
      music: require("@/assets/bj_music.mp3"),
      tableData: [], //中奖名单,
      one: [],
      two: [],
      three: [],
    };
  },
  created: function () {
    const that = this;
    that.tableData =this.$route.params.data;
    // console.log("arr"+arr);
        for (var i = 0, len = that.tableData.length; i < len; i += 1) {
          if (that.tableData[i]["zjbz"] == 1) {
            that.one.push(that.tableData[i]);
          } else if (that.tableData[i]["zjbz"] == 2) {
            that.two.push(that.tableData[i]);
          } else {
            that.three.push(that.tableData[i]);
            console.log(that.three);
          }
        }
  },
  methods: {
    jump() {
      this.$router.push("/home");
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