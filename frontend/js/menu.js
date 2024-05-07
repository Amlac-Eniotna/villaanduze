function menuMobile() {
  let menu = document.querySelector('.menu-mobile-off')
  let checkboxMenu = document.querySelector('.menu-mobile input')
  checkboxMenu.addEventListener('change', (e) => {
    if (e.target.checked) {
      menu.classList.remove('menu-mobile-off')
    } else {
      menu.classList.add('menu-mobile-off')
    }
  })
}

menuMobile()
