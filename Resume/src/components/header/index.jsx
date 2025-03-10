import React, { Component, Fragment } from "react";
import { withStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
// import Button from '@material-ui/core/Button';

const styles = theme => ({
    appBar: {
        backgroundColor: 'rgba(255, 255, 255, 1)',
        top: 0,
        bottom: 'auto',
    },
    toolBar: {
        // minHeight: '100px',
    },
    title: {
        flexGrow: 1,
        color: '#182153',
        font: 'normal normal normal 30px/1.4em avenir-lt-w01_35-light1475496,sans-serif',
    },
    button: {
        color: '#182153'
    }
});

class Header extends Component {

    render() {
        const { classes } = this.props;

        return (
            <Fragment>
                <AppBar className={classes.appBar}>
                    <Toolbar className={classes.toolBar}>
                        <Typography variant="h6" className={classes.title}>Parthipan J</Typography>
                        {/* <Button className={classes.button}>Experience</Button>
                        <Button className={classes.button}>Skills</Button>
                        <Button className={classes.button}>Projects</Button>
                        <Button className={classes.button}>Education</Button>
                        <Button className={classes.button}>Contact</Button> */}
                    </Toolbar>
                </AppBar>
                <Toolbar id="back-to-top-anchor" />
            </Fragment>
        )
    }
}

export default withStyles(styles)(Header);