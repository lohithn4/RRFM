import React from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import * as actionCreators from '../actions/auth';

import SearchBar from '../containers/search_bar';
import WeatherList from '../containers/weather_list';
function mapStateToProps(state) {
    return {
        isRegistering: state.auth.isRegistering,
        registerStatusText: state.auth.registerStatusText,
    };
}

function mapDispatchToProps(dispatch) {
    return bindActionCreators(actionCreators, dispatch);
}

class Visualization extends React.Component { // eslint-disable-line react/prefer-stateless-function
    render() {
        return (
            <div>
                <SearchBar/>
                <WeatherList/>
            </div>
        );
    }
}

export default Visualization;
