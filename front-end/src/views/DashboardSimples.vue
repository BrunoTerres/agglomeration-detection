<template>

<body class="c-app">
  
  

  <main class="c-main">
    
    <div class="container">
   
      <div class="row">

        <div class="col main-card">
          <CCol >
            <CCard>
              <CCardHeader>
                Estatísticas
                <CBadge color="success" class="float-right">Success</CBadge>
              </CCardHeader>
              
              <CCardBody>

                <div class="col cards-container">  
                  <CRow>
                    <div class="col">
                      <CCol class="cards" >
                        <CWidgetProgress
                          header="Total Pessoas"
                          text="Numero total de pessoas nas dependencias"
                          footer="Total: 73   Permitido: 100"
                          class="card-header-action position-relative"
                          style="right:5px; top:5px"
                          color="warning"
                          :value="73"
                        />
                      </CCol>
                    </div>
                    
                    <div class="w-100"></div>
                    
                    <div class="col">
                      <CCol class="cards" >
                        <CWidgetProgress
                          header="Uso de Máscara"
                          text="Porcentagem de pessoas com máscara"
                          footer="91% Pessoas com mascara"
                          class="card-header-action position-relative"
                          style="right:5px; top:5px"
                          color="success"
                          :value="91"
                        />
                      </CCol>
                    </div>
        
                    <div class="w-100"></div>

                    <div class="col card-3">  
                      <CCol class="cards" col="12" >
                        <CWidgetIcon
                            header="Salas Livres"
                            text="10"
                            color="info"
                          >
                          <CIcon name="cil-laptop" width="24"/>
                        </CWidgetIcon>
                      </CCol>
                    </div>

                    <div class="w-100"></div>
                    
                    <div class="col card-4">
                      <CCol class="cards" col="12" >
                        <CWidgetIcon
                          header="Salas Ocupadas"
                          text="3"
                          color="danger"
                        >
                          <CIcon name="cil-bell" width="24"/>
                        </CWidgetIcon>
                      </CCol>
                    </div>
                  </CRow>  
                </div>

              </CCardBody>
            </CCard>
          </CCol>
        </div>

   

 <div class="w-100"></div>

    <div class="col alert-card">
          <CCol>
            <CCard>
              <CCardHeader>
                Notificações
                <CBadge shape="pill" color="info" class="float-right">3</CBadge>
              </CCardHeader>
              <CCardBody>
                <div>
                <CCardBody v-if="show_alert">
                  <CAlert show color="danger">
                    <h4 class="alert-heading text-center"><big>CUIDADO!!!</big></h4>
                    <p class="text-center">
                     <big> Muitas pessoas no ambiente! </big>
                    </p>
                   
                    <p class="text-center mb-0">
                      Mantenham o distanciamento.
                    </p>
                  </CAlert>
                </CCardBody>
                </div>

                <div>
                <CCardBody v-if="show_alert">
                  <CAlert show color="warning">

                    <h4 class="alert-heading"><big>A sala esta em 75% da sua capacidade ocupada</big></h4>

                  </CAlert>
                </CCardBody>
                </div>

                <div>
                <CCardBody v-if="show_alert">
                  <CAlert show color="warning">
                    <h4 class="alert-heading text-center">Parabéns!!!</h4>
                    <p class="text-center">
                      Vocês estão há 24h mantendo o distanciamento
                    </p>

                  </CAlert>
                </CCardBody>
                </div>

              </CCardBody>
            </CCard>
          </CCol>
    </div>
    </div> 
    
      <div class="row buttons">
          <div class="col bug-button">
            <CCol sm xs="12"  class="text-center mt-3">
              <CHeaderNavLink to="/bugReport">
                <CButton color="danger" shape="pill" variant="ghost" @click="change_state">
                  <CIcon name="cil-lightbulb"/>&nbsp;Bug Report
                </CButton>
              </CHeaderNavLink>
            </CCol>
          </div>
 <!-- 
          <div class="col dashboard-button">  
            <CHeaderNavLink to="/painelAdmin"> 
              <CCol xs=12 class="text-center mt-3">
                <CButton block color="success" shape="pill">Painel Admin</CButton>    
              </CCol>
            </CHeaderNavLink>
          </div>
-->      
      </div>

    </div> 

  </main>

</body>

</template>



<script>
import MainChartExample from './charts/MainChartExample'
import WidgetsDropdown from './widgets/WidgetsDropdown'
import WidgetsBrand from './widgets/WidgetsBrand'

export default {
  name: 'Dashboard',
  components: {
    MainChartExample,
    WidgetsDropdown,
    WidgetsBrand
  },
  data () {
    return {
      alert2: true,
      show_alert: true,
      selected: 'Month',
      tableItems: [
        {
          avatar: { url: 'img/avatars/1.jpg', status: 'success' },
          user: { name: 'Yiorgos Avraamu', new: true, registered: 'Jan 1, 2015' },
          country: { name: 'USA', flag: 'cif-us' },
          usage: { value: 50, period: 'Jun 11, 2015 - Jul 10, 2015' },
          payment: { name: 'Mastercard', icon: 'cib-cc-mastercard' },
          activity: '10 sec ago'
        },
        {
          avatar: { url: 'img/avatars/2.jpg', status: 'danger' },
          user: { name: 'Avram Tarasios', new: false, registered: 'Jan 1, 2015' },
          country: { name: 'Brazil', flag: 'cif-br' },
          usage: { value: 22, period: 'Jun 11, 2015 - Jul 10, 2015' },
          payment: { name: 'Visa', icon: 'cib-cc-visa' },
          activity: '5 minutes ago'
        },
        {
          avatar: { url: 'img/avatars/3.jpg', status: 'warning' },
          user: { name: 'Quintin Ed', new: true, registered: 'Jan 1, 2015' },
          country: { name: 'India', flag: 'cif-in' },
          usage: { value: 74, period: 'Jun 11, 2015 - Jul 10, 2015' },
          payment: { name: 'Stripe', icon: 'cib-stripe' },
          activity: '1 hour ago'
        },
        {
          avatar: { url: 'img/avatars/4.jpg', status: '' },
          user: { name: 'Enéas Kwadwo', new: true, registered: 'Jan 1, 2015' },
          country: { name: 'France', flag: 'cif-fr' },
          usage: { value: 98, period: 'Jun 11, 2015 - Jul 10, 2015' },
          payment: { name: 'PayPal', icon: 'cib-paypal' },
          activity: 'Last month'
        },
        {
          avatar: { url: 'img/avatars/5.jpg', status: 'success' },
          user: { name: 'Agapetus Tadeáš', new: true, registered: 'Jan 1, 2015' },
          country: { name: 'Spain', flag: 'cif-es' },
          usage: { value: 22, period: 'Jun 11, 2015 - Jul 10, 2015' },
          payment: { name: 'Google Wallet', icon: 'cib-google-pay' },
          activity: 'Last week'
        },
        {
          avatar: { url: 'img/avatars/6.jpg', status: 'danger' },
          user: { name: 'Friderik Dávid', new: true, registered: 'Jan 1, 2015' },
          country: { name: 'Poland', flag: 'cif-pl' },
          usage: { value: 43, period: 'Jun 11, 2015 - Jul 10, 2015' },
          payment: { name: 'Amex', icon: 'cib-cc-amex' },
          activity: 'Last week'
        }
      ],
      tableFields: [
        { key: 'avatar', label: '', _classes: 'text-center' },
        { key: 'user' },
        { key: 'country', _classes: 'text-center' },
        { key: 'usage' },
        { key: 'payment', label: 'Payment method', _classes: 'text-center' },
        { key: 'activity' },
      ]
    }
  },
  methods: {
    color (value) {
      let $color
      if (value <= 25) {
        $color = 'info'
      } else if (value > 25 && value <= 50) {
        $color = 'success'
      } else if (value > 50 && value <= 75) {
        $color = 'warning'
      } else if (value > 75 && value <= 100) {
        $color = 'danger'
      }
      return $color
    },
    change_state(){
      this.show_alert = true ? this.show_alert == false : false 
    }
  }
}
</script>

<style>




</style>