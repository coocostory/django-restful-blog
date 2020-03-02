<template>
  <div class="HeaderNav">
    <el-menu
      :default-active="activeIndex"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b"
    >
      <el-menu-item index="1">主页</el-menu-item>
      <el-submenu index="2">
        <template slot="title">课程</template>
        <el-menu-item v-for="course in courses" :key="course.name">{{
          course.name
        }}</el-menu-item>
      </el-submenu>
      <el-menu-item index="3" disabled>新功能</el-menu-item>
    </el-menu>
  </div>
</template>

<script>
import { getCourse } from "network/home.js";
export default {
  name: "HeaderNav",
  data() {
    return {
      activeIndex: "1",
      courses: []
    };
  },
  created() {
    getCourse().then(res => {
      console.log(res.data);
      this.courses = res.data;
    });
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
      this.activeIndex = key;
    }
  }
};
</script>

<style lang="css" scoped></style>
