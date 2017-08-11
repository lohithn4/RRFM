import React from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import * as actionCreators from '../actions/auth';

import BookList from '../containers/book-list';
import BookDetail from '../containers/book-detail';

function mapStateToProps(state) {
    return {
        isRegistering: state.auth.isRegistering,
        registerStatusText: state.auth.registerStatusText,
    };
}

function mapDispatchToProps(dispatch) {
    return bindActionCreators(actionCreators, dispatch);
}

class Analytics extends React.Component { // eslint-disable-line react/prefer-stateless-function
    render() {
        return (
            <div className="col-md-4">
                <BookList />
                <BookDetail />
                <hr />
            </div>
        );
    }
}

export default Analytics;
