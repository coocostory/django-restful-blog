<template>
  <div class="cs">
    <div id="textcard" v-for="course in courses" :key="course.id">
      <el-card class="box-card">
        <div id="coursename">{{ course.name }}</div>
        <div id="courseperiod">{{ course.period }}</div>
        <div id="courseclasses">
          {{ course.classes1 }} / {{ course.classes2 }} / {{ course.classes3 }}
        </div>
      </el-card>
    </div>
  </div>
</template>

<script>
import { getCourse } from "network/home";

export default {
  name: "cs",
  data() {
    return {
      courses: []
    };
  },
  created() {
    getCourse().then(res => {
      console.log(res.data);
      this.courses = res.data;
    });
  }
};
</script>

<style scoped>
.text {
  font-size: 14px;
}

.item {
  padding: 18px 0;
}

.box-card {
  width: 880px;
}

#coursename {
  margin: -7px 0 4px;
  display: inherit;
  font-size: 18px;
  font-weight: 700;
  line-height: 1.5;
}
#courseclasses {
  font-size: 12px;
  font-weight: 400;
  line-height: 20px;
  color: #787878;
}
#textcard {
  margin-bottom: 10px;
}
</style>
