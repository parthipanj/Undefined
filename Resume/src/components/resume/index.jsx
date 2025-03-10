import React, { Component, Fragment } from 'react';
import Fab from '@material-ui/core/Fab';
import KeyboardArrowUpIcon from '@material-ui/icons/KeyboardArrowUp';
import CssBaseline from '@material-ui/core/CssBaseline';
import Header from '../header';
import Profile from '../profile';
import Experience from '../experience';
import Skills from '../skills';
import Projects from '../projects';
import Education from '../education';
import ScrollTop from '../common/ScrollTop';

class Resume extends Component {

    render() {
        return (
            <Fragment>
                <CssBaseline />
                <Header />
                <Profile />
                <Experience />
                <Projects />
                <Skills />
                <Education />
                <ScrollTop {...this.props}>
                    <Fab color="primary" size="small" aria-label="scroll back to top">
                        <KeyboardArrowUpIcon />
                    </Fab>
                </ScrollTop>
            </Fragment>
        )
    }
}

export default Resume;