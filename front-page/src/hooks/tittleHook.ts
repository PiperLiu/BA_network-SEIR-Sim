import { computed, ref, watch } from 'vue'

/**
 * titleValue is a value between [0, 1]
 * prevalence of infection
 */
const titleValue = ref(0.32)

const titleEmojis = [
  '😋', '😊', '😐', '😥', '😨'
]

const titleString = computed(() => {
  for (let i = 0; i < titleEmojis.length; i++) {
    const val = titleValue.value * titleEmojis.length
    if (val < i + 1 && val >= i) {
      return `${titleEmojis[i]} Infection's ${(titleValue.value * 100).toFixed(0)}% now!`
    }
  }
  return `${titleEmojis[titleEmojis.length - 1]} Infection's ${(titleValue.value * 100).toFixed(0)}% now!`
})

watch(titleValue, () => {
  document.title = titleString.value
})

export {
  titleValue
}
