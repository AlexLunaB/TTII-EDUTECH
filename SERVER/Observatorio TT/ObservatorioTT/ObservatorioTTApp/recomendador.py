

from sklearn.cluster import KMeans
from scipy.sparse import dok_matrix, csr_matrix
import numpy as np

from recursos.models import Rating, Cluster
from usuarios.models import Usuario
import numpy as np
import pandas as pd
import scipy.optimize

def update_clusters():

  num_reviews = Rating.objects.count()
  print(num_reviews)
  update_step = ((num_reviews / 100) + 1) * 5
  print(update_step)
  print(num_reviews % update_step)
  if num_reviews % update_step > 0:  # using some magic numbers here
    # create a sparse matrix from user reviews
    all_user_names = map(lambda x: x.username, Usuario.objects.only("username"))
    all_wine_id = set(map(lambda x: x.recurso.id, Rating.objects.only("recurso")))
    print(all_user_names)
    num_users = len(list(all_user_names))
    ratings_m = dok_matrix((num_users, max(all_wine_id) + 1), dtype=np.fload32)
    print(ratings_m)
    for i in range(num_users):  # each user corresponds to a row, in the order of all_user_names
      user_revies = Rating.objects.filter(user_name=all_user_names[i])
      for user_review in user_revies:
        ratings_m[i, user_review.recurso.id] = user_review.rating

    # Perform kmeans clustering
    k = int(num_users / 10) + 2
    kmeans = KMeans(n_clusters=k)
    clustering = kmeans.fit(ratings_m.tocsr())
    print(kmeans)
    # convert our dok_matrix (dictionary of keys) into csr_matrix (compressed sparse row)

    # Update clusters
    Cluster.objects.all().delete()
    new_clusters = {i: Cluster(name=i) for i in range(k)}
    for cluster in new_clusters.values():  # clusters need to be saved before referring to users
      cluster.save()
    for i, cluster_label in enumerate(clustering.labels_):
      new_clusters[cluster_label].users.add(Usuario.objects.get(username=all_user_names[i]))





def Myrecommend():
  def normalizeRatings(myY, myR):
    # The mean is only counting movies that were rated
    Ymean = np.sum(myY, axis=1) / np.sum(myR, axis=1)
    Ymean = Ymean.reshape((Ymean.shape[0], 1))
    return myY - Ymean, Ymean

  def flattenParams(myX, myTheta):
    return np.concatenate((myX.flatten(), myTheta.flatten()))

  def reshapeParams(flattened_XandTheta, mynm, mynu, mynf):
    assert flattened_XandTheta.shape[0] == int(mynm * mynf + mynu * mynf)
    reX = flattened_XandTheta[:int(mynm * mynf)].reshape((mynm, mynf))
    reTheta = flattened_XandTheta[int(mynm * mynf):].reshape((mynu, mynf))
    return reX, reTheta

  def cofiCostFunc(myparams, myY, myR, mynu, mynm, mynf, mylambda=0.):
    myX, myTheta = reshapeParams(myparams, mynm, mynu, mynf)
    term1 = myX.dot(myTheta.T)
    term1 = np.multiply(term1, myR)
    cost = 0.5 * np.sum(np.square(term1 - myY))
    # for regularization
    cost += (mylambda / 2.) * np.sum(np.square(myTheta))
    cost += (mylambda / 2.) * np.sum(np.square(myX))
    return cost

  def cofiGrad(myparams, myY, myR, mynu, mynm, mynf, mylambda=0.):
    myX, myTheta = reshapeParams(myparams, mynm, mynu, mynf)
    term1 = myX.dot(myTheta.T)
    term1 = np.multiply(term1, myR)
    term1 -= myY
    Xgrad = term1.dot(myTheta)
    Thetagrad = term1.T.dot(myX)
    # Adding Regularization
    Xgrad += mylambda * myX
    Thetagrad += mylambda * myTheta
    return flattenParams(Xgrad, Thetagrad)

  df = pd.DataFrame(list(Rating.objects.all().values()))
  mynu = df.user_id.unique().max()
  mynm = df.recurso_id.unique().max()
  mynf = 10
  Y = np.zeros((mynm, mynu))
  for row in df.itertuples():
    Y[row[6] - 1, row[2] - 1] = row[7]
  R = np.zeros((mynm, mynu))
  for i in range(Y.shape[0]):
    for j in range(Y.shape[1]):
      if Y[i][j] != 0:
        R[i][j] = 1

  Ynorm, Ymean = normalizeRatings(Y, R)
  X = np.random.rand(mynm, mynf)
  Theta = np.random.rand(mynu, mynf)
  myflat = flattenParams(X, Theta)
  mylambda = 12.2
  result = scipy.optimize.fmin_cg(cofiCostFunc, x0=myflat, fprime=cofiGrad, args=(Y, R, mynu, mynm, mynf, mylambda),
                                  maxiter=40, disp=True, full_output=True)
  resX, resTheta = reshapeParams(result[0], mynm, mynu, mynf)
  prediction_matrix = resX.dot(resTheta.T)
  return prediction_matrix, Ymean
