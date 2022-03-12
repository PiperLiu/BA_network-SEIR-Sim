<script setup lang="ts">
import { withDefaults, defineProps, computed, defineEmits } from 'vue'

type Range = [number, number]

interface Props {
  valueName: string
  modelValue: number
  range?: Range
  isInteger?: boolean
  isRunButton?: boolean
  runButtonRuning?: boolean
  isOneRow?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  range: () => [0, 1],
  isInteger: false,
  isRunButton: false,
  runButtonRuning: false,
  isOneRow: false
})

const emits = defineEmits(
  ['update:modelValue']
)

/**
 * v-model 不能直接绑定 props
 * 因为 props 的值不能是 mutation 的
 * 这里参考官方文档使用计算属性
 */
const value = computed({
  get: () => {
    if (props.isInteger) {
      return Math.floor(props.modelValue)
    }
    if (props.modelValue < props.range[0]) return props.range[0]
    if (props.modelValue > props.range[1]) return props.range[1]
    return props.modelValue
  },
  set: (val) => {
    if (props.isInteger) {
      val = Math.floor(val)
    }
    if (val < props.range[0]) val = props.range[0]
    if (val > props.range[1]) val = props.range[1]
    emits('update:modelValue', val)
  }
})

</script>

<template>
  <div class="controller">
    <div class="row first__row">
      {{ valueName }}
      <button class="run" v-if="isRunButton"></button>
      <input class="value__input"
        :placeholder="`[${range[0]}~${range[1]}], ${isInteger ? 'int' : 'float'}`"
        v-model="value"
      />
    </div>
    <div class="row second__row">
      <input type="range" class="range__input"
        v-model="value"
        :min="range[0]"
        :max="range[1]"
        :step=" isInteger ? 1 : 0.01 "
      />
    </div>
  </div>
</template>

<style>
.controller {
  display: flex;
}

</style>
