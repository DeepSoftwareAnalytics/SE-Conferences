# -*- coding: utf-8 -*-
"""A plotting utility for conference stats
"""
# Author: Yue Zhao <yuezhao@cs.toronto.edu>
# License: BSD 2 clause


import numpy as np
import matplotlib.pyplot as plt

import matplotlib

# rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

n_groups = 3

submitted_2016 = np.asarray([530,280 ,273])
accepted_2016 = np.asarray([101, 60, 74])
rejected_2016 = submitted_2016 - accepted_2016
accp_rate_2016 = np.rint((accepted_2016 / submitted_2016) * 100).astype(int)

submitted_2017 = np.asarray([415, 314, 295])
accepted_2017 = np.asarray([68, 65, 72, ])
rejected_2017 = submitted_2017 - accepted_2017
accp_rate_2017 = np.rint((accepted_2017 / submitted_2017) * 100).astype(int)

submitted_2018 = np.asarray([502,346, 289])
accepted_2018 = np.asarray([105, 83, 61])
rejected_2018 = submitted_2018 - accepted_2018
accp_rate_2018 = np.rint((accepted_2018 / submitted_2018) * 100).astype(int)

submitted_2019 = np.asarray([529, 445, 303])
accepted_2019 = np.asarray([109, 93,74,])
rejected_2019 = submitted_2019 - accepted_2019
accp_rate_2019 = np.rint((accepted_2019 / submitted_2019) * 100).astype(int)


submitted_2020 = np.asarray([617, 414, 360])
accepted_2020 = np.asarray([129,93, 101])
rejected_2020 = submitted_2020 - accepted_2020
accp_rate_2020 = np.rint((accepted_2020 / submitted_2020) * 100).astype(int)

fig, ax = plt.subplots()

fig.set_size_inches(20, 8)

index = np.arange(n_groups)
bar_width = 0.19

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects2016_rejected = ax.bar(index,
                            rejected_2016,
                            bar_width,
                            alpha=opacity,
                            color='darkred',
                            error_kw=error_config,
                            label='2016_rejected')

rects2016_accepted = ax.bar(index,
                            accepted_2016,
                            bar_width,
                            bottom=rejected_2016,
                            alpha=opacity,
                            color='red',
                            error_kw=error_config,
                            label='2016_accepted')

rects2016 = ax.bar(index,
                   submitted_2016,
                   bar_width,
                   alpha=0.2,
                   color='white',
                   error_kw=error_config,
                   #                label='2016'
                   )

rects2017_rejected = ax.bar(index + bar_width,
                            rejected_2017,
                            bar_width,
                            alpha=opacity,
                            color='darkgreen',
                            error_kw=error_config,
                            label='2017_rejected')

rects2017_accepted = ax.bar(index + bar_width,
                            accepted_2017,
                            bar_width,
                            bottom=rejected_2017,
                            alpha=opacity,
                            color='mediumseagreen',
                            error_kw=error_config,
                            label='2017_accepted')

rects2017 = ax.bar(index + bar_width,
                   submitted_2017,
                   bar_width,
                   alpha=0.2,
                   color='white',
                   error_kw=error_config,
                   #                label='2017'
                   )

rects2018_rejected = ax.bar(index + bar_width * 2,
                            rejected_2018,
                            bar_width,
                            alpha=opacity,
                            color='darkblue',
                            error_kw=error_config,
                            label='2018_rejected')

rects2018_accepted = ax.bar(index + bar_width * 2,
                            accepted_2018,
                            bar_width,
                            bottom=rejected_2018,
                            alpha=opacity,
                            color='slateblue',
                            error_kw=error_config,
                            label='2018_accepted')

rects2018 = ax.bar(index + bar_width * 2,
                   submitted_2018,
                   bar_width,
                   alpha=0.2,
                   color='white',
                   error_kw=error_config,
                   #                label='2018'
                   )

rects2019_rejected = ax.bar(index + bar_width * 3,
                            rejected_2019,
                            bar_width,
                            alpha=opacity,
                            color='yellow',
                            error_kw=error_config,
                            label='2019_rejected')

rects2019_accepted = ax.bar(index + bar_width * 3,
                            accepted_2019,
                            bar_width,
                            bottom=rejected_2019,
                            alpha=opacity,
                            color='y',
                            error_kw=error_config,
                            label='2019_accepted')

rects2019 = ax.bar(index + bar_width * 3,
                   submitted_2019,
                   bar_width,
                   alpha=0.2,
                   color='white',
                   error_kw=error_config,
                   #                label='2019'
                   )

rects2020_rejected = ax.bar(index + bar_width * 4,
                            rejected_2020,
                            bar_width,
                            alpha=opacity,
                            color='darkmagenta',
                            error_kw=error_config,
                            label='2020_rejected')

rects2020_accepted = ax.bar(index + bar_width * 4,
                            accepted_2020,
                            bar_width,
                            bottom=rejected_2020,
                            alpha=opacity,
                            color='m',
                            error_kw=error_config,
                            label='2020_accepted')

rects2020 = ax.bar(index + bar_width * 4,
                   submitted_2020,
                   bar_width,
                   alpha=0.2,
                   color='white',
                   error_kw=error_config,
                   #                label='2020'
                   )

ax.set_xlabel('Major SE Conferences', fontsize=20)
ax.set_ylabel('# Papers & Acceptance Rate', fontsize=20)
ax.set_title('Conference Statistics (2016-2020)', fontsize=20)
ax.set_xticks(index + bar_width)
# ax.set_xticklabels(('KDD', 'SDM', 'ICDM', 'CIKM', 'PKDD', 'WSDM', 'PAKDD'))
ax.set_xticklabels(('ICSE', 'ASE', 'FSE',),fontsize=20)
ax.legend(fontsize=16,ncol=3)


def autolabel(rects, accp_rates, accps, rejs):
    """
    Attach a text label above each bar displaying relevant information
    """
    for rect, accp_rate, accp, rej in zip(rects, accp_rates, accps, rejs):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., height + 10,
                str(accp_rate) + '%',
                ha='center', va='bottom',fontsize=15)
        ax.text(rect.get_x() + rect.get_width() / 2., 0.9 * height,
                '%d' % int(accp),
                ha='center', va='bottom',fontsize=15)
        ax.text(rect.get_x() + rect.get_width() / 2., 0.4 * height,
                '%d' % int(rej),
                ha='center', va='bottom',fontsize=15)


autolabel(rects2016, accp_rate_2016, accepted_2016, rejected_2016)
autolabel(rects2017, accp_rate_2017, accepted_2017, rejected_2017)
autolabel(rects2018, accp_rate_2018, accepted_2018, rejected_2018)
autolabel(rects2019, accp_rate_2019, accepted_2019, rejected_2019)
autolabel(rects2020, accp_rate_2020, accepted_2020, rejected_2020)
plt.savefig('conference_stats_se.png', dpi=330)
plt.show()