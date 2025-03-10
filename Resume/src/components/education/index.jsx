import React, { Component, Fragment } from 'react';
import { withStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import Typography from '@material-ui/core/Typography';
import Divider from '@material-ui/core/Divider';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import { educations } from '../../static/json/educations';

const styles = theme => ({
    root: {
        flexGrow: 1,
        backgroundColor: 'white',
    },
    text: {
        padding: theme.spacing(3, 0, 3),
        textTransform: "uppercase",
        textAlign: 'center',
    },
    gridItem: {
        margin: 'auto',
        width: 850,
        height: '100%',
        maxWidth: '100%',
        maxHeight: '100%',
    },
    cardRoot: {
        display: 'flex',
        width: '100%',
    },
    details: {
        display: 'flex',
        flexDirection: 'column',
        textAlign: 'end',
        width: '50%',
    },
    cardContent: {
        width: '50%',
    }
});

class Education extends Component {

    render() {
        const { classes } = this.props;

        return (
            <Fragment>
                <Container className={classes.root}>
                    <Typography className={classes.text} variant="h5">
                        Education
                    </Typography>
                </Container>
                <Container className={classes.root}>
                    <List>
                        {educations.map((education, index) => {
                            return (
                                <ListItem key={index} className={classes.gridItem}>
                                    <Card className={classes.cardRoot} elevation={0}>
                                        <CardContent border={0} className={classes.details}>
                                            <Typography component='h5' variant='h5'>{`${education.startDate} - ${education.endDate}`}</Typography>
                                            <Typography variant='subtitle1' color='textSecondary'>{`${education.studyType} in ${education.area}`}</Typography>
                                        </CardContent>
                                        <Divider orientation='vertical' flexItem />
                                        <CardContent border={0} className={classes.cardContent}>
                                            <Typography component='h6' variant='h6'>{`${education.institution}`}</Typography>
                                            <Typography variant='subtitle1' color='textSecondary'>{education.location}</Typography>
                                            <Typography variant='subtitle2' color='textSecondary'>{`GPA: ${education.gpa}`}</Typography>
                                        </CardContent>
                                    </Card>
                                </ListItem>
                            )
                        })}
                    </List>
                </Container>
            </Fragment >
        );
    }
}

export default withStyles(styles)(Education);