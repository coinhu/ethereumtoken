import React from "react"
import PropTypes from "prop-types"
import { bindActionCreators } from "redux"
import { connect } from "react-redux"
import { withRouter } from "react-router-dom"
import styled from "styled-components"
import { Button } from "antd"

import { action } from "../_shared/redux-actions"

// ----------------------------------------------------------------------------

export class Dashboard extends React.Component {
  static propTypes = {
    className: PropTypes.string.isRequired,
  }

  // -------------------------------------

  state = {}

  // -------------------------------------

  componentWillMount() {}

  componentWillReceiveProps(nextProps) {}

  componentWillUnmount() {}

  // -------------------------------------

  render() {
    const { user } = this.props
    const { value } = this.state

    return <div className={this.props.className}>TODO</div>
  }
}

// ----------------------------------------------------------------------------
// Router wrapper
// ----------------------------------------------------------------------------

const DashboardWithRouter = withRouter(Dashboard)

// ----------------------------------------------------------------------------
// Redux wrapper
// ----------------------------------------------------------------------------

const mapStateToProps = (state, ownProps) => {
  return {
    user: state.user.user,
  }
}

const mapDispatchToProps = (dispatch, ownProps) => {
  return bindActionCreators({ action }, dispatch)
}

const DashboardWithRedux = connect(mapStateToProps, mapDispatchToProps)(
  DashboardWithRouter
)

// ----------------------------------------------------------------------------
// Styled components wrapper
// ----------------------------------------------------------------------------

const StyledDashboard = styled(DashboardWithRedux)`
  & {
  }
`
// ----------------------------------------------------------------------------

export default StyledDashboard
